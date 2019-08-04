# from GoogleNews import GoogleNews
# googlenews = GoogleNews()
# print(googlenews.search('India'))
#
#
# print(googlenews.gettext())
# # print(googlenews.getlinks())

# from django.shortcuts import render
from GoogleNews import GoogleNews
googlenews = GoogleNews()

googlenews.search('IndiA')
def news():
    for p in googlenews.gettext():
        return render(request, "results.html",{'name':p})
