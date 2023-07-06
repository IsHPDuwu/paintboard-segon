from django.shortcuts import render, HttpResponse
from index.__init__ import mapp

# Create your views here.


def getboard(request):
    ret = st = nd = rd = ""
    for y in range(0, 999):
        for x in range(0, 599):
            st, nd, rd = [str(hex(mapp[x][y][0]))[2:], str(
                hex(mapp[x][y][1]))[2:], str(hex(mapp[x][y][2]))[2:]]
            while (st.__len__() < 2):
                st = "0"+st
            while (nd.__len__() < 2):
                nd = "0"+nd
            while (rd.__len__() < 2):
                rd = "0"+rd
            ret += st + nd + rd
        ret += '\n'
    # print(ret)
    return HttpResponse(ret)


def paintboard(request):
    if request.method == 'GET':
        return HttpResponse('This is a POST page.')
    elif request.method == 'POST':
        mapp[int(request.POST['y'])][int(request.POST['x'])] = [int(request.POST['color'][0:2], 16), int(
            request.POST['color'][2:4], 16), int(request.POST['color'][4:6], 16)]
        print(request.POST['uid'] + " paint " +
              request.POST['color'] + " at " + request.POST['x'] + " " + request.POST['y'])
        return HttpResponse("200")
        # return HttpResponse(request.POST['uid'] + " paint " + request.POST['color'] + " at " + request.POST['x'] + " " + request.POST['y'])
    else:
        pass


def index(request):
    return render(request, "index.html")
