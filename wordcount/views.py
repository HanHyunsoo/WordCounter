from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')


def count(request):
    full_text = request.GET['fulltext']

    # word 단어 세기
    word_list = full_text.split()
    word_dictionary = {}

    # 아스키 코드 세기
    word_list2 = list(full_text)
    ASCII_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    for i in word_list2:
        if ord(i) in ASCII_dictionary:
            ASCII_dictionary[ord(i)] += 1
        else:
            ASCII_dictionary[ord(i)] = 1

    return render(request, 'wordcount/count.html',{'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items(), 'dictionary2': ASCII_dictionary.items()})