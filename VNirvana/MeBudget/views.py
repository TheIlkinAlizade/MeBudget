import random
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

# Create your views here.


def index(request):
    motivation = ""
    motivation = get_random_motivation_messages()

    return render(request, "MeBudget/index.html", {"text": motivation})



def login(request):
    return render(request, "Mebudget/login.html")
'''

def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"datas/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))

   if request.method == "POST":
        entry_title = request.POST['entry_title']
        textarea = request.POST['new_entry']
        if util.get_entry(entry_title):
            return render(request, "encyclopedia/create_new_page.html",{"text": error_message}) 
        else:
            util.save_entry(entry_title, textarea)
            return HttpResponseRedirect(reverse('entry', kwargs={'name': entry_title}))
    else:
        return render(request, "encyclopedia/create_new_page.html",{"text": ""})
'''


def get_random_motivation_messages():
    motivation_messages = [
        "You're doing great! However, your expenses seem a bit below your budget. Save more to reach bigger goals in the future.",
        "Every step is a big change. Keep your budget under control and move forward on the path to success!",
        "Having a plan is the key to success. Review your expenses and achieve your financial goals!",
        "Managing your money is a way to control your future. Pay attention to your daily expenses and save!",
        "Small steps lead to big success. Track your expenses and be patient to reach your financial goals!",
        "Take a step every day to achieve future successes. Managing your budget correctly is the way to success.",
        "Your future successes depend on your current financial decisions. Keep your expenses under control and reach your goals!",
        "Managing your budget is a step towards building the life of your dreams. Shape your future by saving!",
        "Take small steps to reach your financial goals. Every saving makes your future brighter!",
        "Use your budget to achieve your financial goals. Controlled expenses will lead you to financial success.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
        "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "Success is not in what you have, but who you are. - Bo Bennett",
        "The best way to predict the future is to create it. - Peter Drucker",
        "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
        # ... Eklemeleri buraya yapabilirsiniz
    ]

    selected_message = random.choice(motivation_messages)
    return selected_message