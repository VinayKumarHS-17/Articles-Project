from django.shortcuts import render

# Create your views here.

titles=[
    {   'id':'1',
        't':'The Importance of Getting Quality Sleep for Your Health',
        'desc':'Quality sleep is essential for maintaining good health and mental clarity. A consistent sleep schedule improves memory, boosts immunity, and lowers stress. Simple practices like reducing screen time and creating a calming bedtime routine can lead to better rest and overall wellness.',
        'author':'James Carter'
    },
    {
        'id':'2',
        't':'How Staying Hydrated Can Boost Your Energy and Focus',
        'desc':'Hydration is key to feeling energized and focused throughout the day. Water supports digestion, keeps joints healthy, and helps maintain clear thinking. Staying hydrated by drinking water and eating water-rich foods like fruits and vegetables can make a big difference in your energy levels.',
        'author':'Sophia Bennett'
    },
    {
        'id':'3',
        't':'Lifelong Learning: The Benefits of Continuing to Grow Your Knowledge',
        'desc':"Continuing to learn as we age keeps the mind sharp and opens doors to new experiences. Whether it's reading, learning a language, or picking up a new skill, lifelong learning keeps us engaged and adaptable, bringing more joy and purpose to everyday life.",
        'author':'Daniel Roberts'
    },
    {
        'id':'4',
        't':'Practicing Gratitude: A Simple Habit for Lasting Happiness',
        'desc':"Making gratitude a daily practice can greatly improve your mood and outlook on life. Taking a moment each day to reflect on things you're thankful for – big or small – can reduce stress, strengthen relationships, and bring a sense of peace and happiness to your life.",
        'author':'Emily Harrison'
    },
    {
        'id':'5',
        't':'How Spending Time in Nature Can Improve Your Health and Mood',
        'desc':"Spending time outdoors offers natural benefits for both body and mind. Fresh air and natural light can reduce stress, improve mood, and increase energy. Whether it's a walk in the park or relaxing in your backyard, connecting with nature is a simple way to feel happier and healthier.",
        'author':'Michael Turner'
    },
]


all_events = [
    {"title": "Tech Conference 2025", "date": "05-02-2025", "payment_amount": 1500},
    {"title": "AI Workshop", "date": "10-02-2025", "payment_amount": 800},
    {"title": "Blockchain Summit", "date": "12-02-2025", "payment_amount": 2200},
    {"title": "Data Science Symposium", "date": "14-02-2025", "payment_amount": 1600},
    {"title": "UI/UX Design Workshop", "date": "15-02-2025", "payment_amount": 700},
]


daily_events=[
    {"title": "Django Meetup", "date": "20-02-2025", "payment_amount": 500},
    {"title": "Python Bootcamp", "date": "20-02-2025", "payment_amount": 1200},
    {"title": "Startup Pitch Event", "date": "20-02-2025", "payment_amount": 2000},
    {"title": "Cybersecurity Seminar", "date": "20-02-2025", "payment_amount": 950},
    {"title": "Cloud Computing Expo", "date": "20-02-2025", "payment_amount": 1800},
]

def home(request):
    all_eve={'all_events':all_events}
    return render(request, 'home.html',all_eve)


def about(request):
    return render(request, 'about.html')

def events(request):
    daily={'daily_events':daily_events}
    return render(request, 'events.html',daily)

def article(request):
    app = {'titles':titles}
    return render(request, 'article.html',app)

def construction(request):
    return render(request, 'construction.html')

