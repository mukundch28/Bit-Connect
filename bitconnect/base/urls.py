from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$' , views.index , name="index") ,
    url(r'^signin$' , views.signin , name = 'signin') , 
    url(r'^logout' , views.logouts , name = 'logout') ,
    url(r'^unfriend/(?P<mem_id>[0-9]+)$' , views.unfriend , name = 'unfriend') ,
    url(r'^profile/(?P<mem_id>[0-9]+)/myposts$' , views.my_posts , name = 'myposts') ,
    url(r'^profile/posts$' , views.posts , name = 'posts') ,
    url(r'^profile/friends$' , views.friends , name = 'friends') ,
    url(r'^profile/friendrequests$' , views.friendrequests , name = 'friendrequests') ,
    url(r'^profile/friends/unfriend/(?P<mem_id>[0-9]+)$' , views.mainunfriend , name = 'mainunfriend') ,
    url(r'^post/(?P<post_id>[0-9]+)$' , views.postdetail , name = 'postdetail' ) ,
    url(r'^post/(?P<post_id>[0-9]+)/edit$' , views.editpost , name='editpost') ,
    url(r'^post/(?P<post_id>[0-9]+)/delete$' , views.delete , name='deletepost') ,
    url(r'^post/(?P<post_id>[0-9]+)/like$' , views.like , name = 'like' ) ,
    url(r'^post/(?P<post_id>[0-9]+)/dislike$' , views.dislike , name = 'dislike' ) ,
    url(r'^posts/(?P<post_id>[0-9]+)/like$' , views.plike , name = 'plike' ) ,
    url(r'^posts/(?P<post_id>[0-9]+)/dislike$' , views.pdislike , name = 'pdislike' ) ,
    url(r'^posts/(?P<post_id>[0-9]+)/plike$' , views.pplike , name = 'pplike' ) ,
    url(r'^posts/(?P<post_id>[0-9]+)/pdislike$' , views.ppdislike , name = 'ppdislike' ) ,
    url(r'^comment/(?P<comment_id>[0-9]+)/delete$' , views.commentdelete , name='deletecomment') ,
    url(r'^profile/acceptrequest/(?P<mem_id>[0-9]+)$' , views.profacceptrequest , name='profacceptrequest') ,
    url(r'^profile/sendrequest/(?P<mem_id>[0-9]+)$' , views.profsendrequest , name='profsendrequest') ,
    url(r'^profile/deleterequest/(?P<mem_id>[0-9]+)$' , views.profdeleterequest , name='profdeleterequest') ,
    url(r'^profile/rejectrequest/(?P<mem_id>[0-9]+)$' , views.profrejectrequest , name='profrejectrequest') ,
    url(r'^profile/friendrequests/acceptrequest/(?P<mem_id>[0-9]+)$' , views.reqacceptrequest , name='reqacceptrequest') ,
    url(r'^profile/friendrequests/rejectrequest/(?P<mem_id>[0-9]+)$' , views.reqrejectrequest , name='reqrejectrequest') ,
    url(r'^profile/friendrequests/deleterequest/(?P<mem_id>[0-9]+)$' , views.reqdeleterequest , name='reqdeleterequest') ,
    url(r'^profile/friends/deleterequest/(?P<mem_id>[0-9]+)$' , views.frideleterequest , name='frideleterequest') ,
    url(r'^profile/findpeople$' , views.find , name='findpeople' ) ,
    url(r'^profile/findpeople/acceptrequest/(?P<mem_id>[0-9]+)$' , views.findacceptrequest , name='findacceptrequest') ,
    url(r'^profile/findpeople/deleterequest/(?P<mem_id>[0-9]+)$' , views.finddeleterequest , name='finddeleterequest') ,
    url(r'^profile/findpeople/sendrequest/(?P<mem_id>[0-9]+)$' , views.findsendrequest , name='findsendrequest') ,
    url(r'^profile/findpeople/rejectrequest/(?P<mem_id>[0-9]+)$' , views.findrejectrequest , name='findrejectrequest') ,
    url(r'^profile/prof_pic$' , views.prof_pic , name="prof_pic") ,
    url(r'^profile/bio' , views.editbio , name="editbio") ,
]
