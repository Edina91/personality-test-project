from django.shortcuts import render

# Define your questions and options
QUESTIONS = [
    {
        'id': 1,
        'question': 'You find it takes effort to introduce yourself to other people.',
        'options': ['Agree', 'Neutral', 'Disagree']
    },
    {
        'id': 2,
        'question': 'You consider yourself more practical than creative.',
        'options': ['Agree', 'Neutral', 'Disagree']
    },
    {
        'id': 3,
        'question': 'Winning a debate matters less to you than making sure no one gets upset.',
        'options': ['Agree', 'Neutral', 'Disagree']
    },
]

def quiz_view(request):
    if request.method == 'POST':
        answers = []
        for q in QUESTIONS:
            answer = request.POST.get(str(q['id']))
            answers.append(answer)
        # Simple logic to calculate result
        agree_count = answers.count('Agree')
        if agree_count > len(QUESTIONS) / 2:
            result = 'You are an extrovert!'
        else:
            result = 'You are an introvert!'
        return render(request, 'result.html', {'result': result})
    return render(request, 'quiz.html', {'questions': QUESTIONS})

def about(request):
    return render(request, 'about.html')
