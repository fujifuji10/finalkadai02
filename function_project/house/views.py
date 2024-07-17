from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Housing, HouseComments
from django.http import Http404

# Create your views here.
def regist_house(request):
  regist_house_form = forms.RegistHouseForm(request.POST or None)
  if regist_house_form.is_valid():
    regist_house_form.instance.user=request.user #現在ログインしているユーザーを取得できて、そのユーザーが作成したという意味になる
    regist_house_form.save() #themeにuserが外部キーで入っているため、誰がタイトルを作成したかを記載する必要がある↑①行上
    messages.success(request, '物件が登録されました')
    return redirect('house:list_house')
  return render(
    request, 'house/regist_house.html', context={
      'regist_house_form':regist_house_form,
    }
  )
  
def list_house(request):
  house = Housing.objects.fetch_all_housing()
  return render(
  request, 'house/list_house.html', context={
    'house':house
  }
  )
  
def detail_house(request):
  return render(
  request, 'house/detail_house.html', 
  )
  
def edit_house(request, id):
  house = get_object_or_404(Housing, id=id) #Housingをidからget_object_or_404から取得します
  if house.user.id != request.user.id: #ログイン者のuser.idと編集希望者のリクエストのuser.idが違っていればエラーを発生させる
    raise Http404
  edit_house_form = forms.EditHouseForm(request.POST or None, instance=house)
  if edit_house_form.is_valid():
    edit_house_form.save()
    messages.success(request, '物件情報を更新しました')
    return redirect('house:list_house')
  return render( #上のリダイレクトする場合以外は以下を渡してね（返す）
    request, 'house/edit_house.html', context={
      'edit_house_form':edit_house_form,
      'id':id, #引数のIDをそのまま渡す
    }
  )
  
def delete_house(request, id):
  house = get_object_or_404(Housing, id=id)
  if house.user.id != request.user.id:
    raise Http404
  delete_house_form = forms.DeleteHouseForm(request.POST or None)
  if delete_house_form.is_valid(): #csrf_tokenのチェック！
    house.delete()
    messages.success(request, '物件を削除しました')
    return redirect('house:list_house')
  return render(
    request, 'house/delete_house.html', context={
      'delete_house_form':
        delete_house_form
    }
  )
  
def post_house_comments(request, house_id):
  post_house_comment_form = forms.PostHouseCommentForm(request.POST or None) #requestを送信した結果をコメントモデルに挿入するためのform
  house = get_object_or_404(Housing, id=house_id)
  comments = HouseComments.objects.fetch_by_house_id(house_id) #テーマに対してのコメントを全て取得
  if post_house_comment_form.is_valid():
    post_house_comment_form.instance.house = house #作成されたテーマが対象
    post_house_comment_form.instance.user = request.user #ログインしているログインユーザーが対象
    post_house_comment_form.save() #ここまでだとどのテーマに対するコメント？誰がコメント？かわからないので要素を入れる
    return redirect('house:post_house_comments', house_id=house_id)
  return render(
    request, 'house/post_house_comments.html', context={
      'post_house_comment_form':post_house_comment_form,
      'comments':comments,
    }
  )
  