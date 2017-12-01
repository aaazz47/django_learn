from django.test import TestCase

# Create your tests here.
import datetime

from django.urls import reverse
from django.utils import timezone

from .models import Question


class QuestionModelsTests(TestCase):
    
    def test_was_published_recently_with_future_qusetion(self):
        """
        当 questions 的创建在未来时 was_published_recently() 应当返回 False
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


def create_question(question_text, days):
    """
    创建一个 question 并设定 question_text 和创建时间的偏移量 days (过去发布的问卷是负数，
    将来发布的问卷是正数)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        """
        如果没有问卷存在则显示一条适当的信息。
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "没有问卷调查。")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_past_question(self):
        """
        问卷的创建时间如果是过去，则在 index 页面显示
        """
        create_question(question_text="Past question.",days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )
    
    def test_future_question(self):
        """
        问卷创建时间在将来的，则不在 index 页面显示
        """
        create_question(question_text='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, '没有问卷调查。')
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_future_question_and_past_question(self):
        """
        如果同时存在过去和将来创建的问卷，则只有过去创建的显示
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )
    
    def test_two_past_question(self):
        """
        如果有两个过去创建的问卷，则两个都应该显示
        """
        create_question(question_text='Past question 1.', days=-30)
        create_question(question_text='Past question 2.', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 1.>','<Question: Past question 2.>']
        )


class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        """
        如果 detail 视图遇到未发行的问卷，则返回 404 错误
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_past_question(self):
        """
        如果 detail 视图遇到已发行的问卷，则显示问卷的 question_text
        """
        past_question = create_question(question_text='Past question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
