from django.db import models
from django.contrib.auth.models import User

ACTIVITY_CHOICES = (
    ("Completed", "Completed"),
    ("Pending", "Pending"),
)

DAY_CHOICES = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
)

TITLE_CHOICES = (
    (
        "Coding", (
            ("Python Development", "Python Development"),
            ("JavaScript Development", "JavaScript Development"),
            ("TypeScript Development", "TypeScript Development")
        )
    ),
    (
        "Full-Stack", (
            ("Django Development", "Django Development"),
        )
    ),
    (
        "Frontend", (
            ("ReactJs Development", "ReactJs Development"),
            ("NextJs Development", "NextJs Development"),
        )
    ),
    (
        "RESTFUL", (
            ("Node-Express Development", "Node-Express Development"),
            ("Graphql Development", "Graphql Development"),
            ("Django REST Development", "Django REST Development"),
        )
    ),
    (
        "Mobile", (
            ("React-Native Development", "React-Native Development"),
        )
    ),
    (
        "DevOps", (
            ("Docker Development", "Docker Development"),
            ("Kubernetes Development", "Kubernetes Development"),
            ("Cloud Development", "Cloud Development"),
        )
    )
)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, choices=TITLE_CHOICES)
    day = models.CharField(max_length=200, choices=DAY_CHOICES)
    week = models.CharField(max_length=200, default=1)
    status = models.CharField(max_length=200, choices=ACTIVITY_CHOICES, default="Pending")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title