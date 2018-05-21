from django.db import models


class Participant(models.Model):
    login = models.TextField(default=None, primary_key=True)
    name = models.TextField(default=None, null=True)
    score = models.FloatField(default=0, null=True)
    rank = models.IntegerField(default=None, null=True)

    # ranking trend compared to last iteration
    trend = models.IntegerField(default=None, null=True)

    # time of latest action
    last_active_at = models.DateTimeField(default=None, null=True)

    # number of positive reactions received
    pos_in = models.IntegerField(default=0, null=True)

    # weighted positive reactions received
    weighted_pos_in = models.FloatField(default=0, null=True)

    # number of positive reactions give away
    pos_out = models.IntegerField(default=0, null=True)

    # number of negative reactions received
    neg_in = models.IntegerField(default=0, null=True)

    # weighted negative reactions received
    weighted_neg_in = models.FloatField(default=0, null=True)

    # number of negative reactions give away
    neg_out = models.IntegerField(default=0, null=True)

    # punishment points
    punishment = models.FloatField(default=0, null=True)

    # weight factor
    weight_factor = models.FloatField(default=0.1, null=True)

    def __str__(self):
        return 'Meta-reviewer: ' + self.login

    class Meta:
        ordering = ['rank']


class Comment(models.Model):
    id = models.TextField(default=None, primary_key=True)
    body = models.TextField(default=None, null=True)
    diff = models.TextField(default=None, null=True)
    created_at = models.DateTimeField(default=None, null=True)
    last_edited_at = models.DateTimeField(default=None, null=True)
    author = models.ForeignKey(Participant, null=True)

    # number of positive reactions received
    pos = models.IntegerField(default=0, null=True)

    # weighted positive reactions received
    weighted_pos = models.FloatField(default=0, null=True)

    # number of negative reactions received
    neg = models.IntegerField(default=0, null=True)

    # weighted negative reactions received
    weighted_neg = models.FloatField(default=0, null=True)

    # review comment score = positive - negative
    score = models.FloatField(default=0, null=True)


class Reaction(models.Model):
    id = models.TextField(default=None, primary_key=True)
    created_at = models.DateTimeField(default=None, null=True)
    content = models.TextField(default=None, null=True)
    giver = models.ForeignKey(Participant, related_name='give', null=True)
    receiver = models.ForeignKey(Participant, related_name='receive', null=True)
    review = models.ForeignKey(Comment, null=True)
