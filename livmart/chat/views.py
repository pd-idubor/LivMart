from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from product.models import Product

from .forms import MessageForm
from .models import Chat


@login_required
def new_chat(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if product.created_by == request.user:
        return redirect('dashboard:index')
    
    chats = Chat.objects.filter(product=product).filter(members__in=[request.user.id])

    if chats:
        return redirect('chat:detail', pk=chats.first().id)

    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            chat = Chat.objects.create(product=product)
            chat.members.add(request.user)
            chat.members.add(product.created_by)
            chat.save()

            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.created_by = request.user
            chat_message.save()

            return redirect('product:detail', pk=product_pk)
    else:
        form = MessageForm()
    
    return render(request, 'new_chat.html', {
        'form': form
    })

@login_required
def inbox(request):
    chats = Chat.objects.filter(members__in=[request.user.id])

    return render(request, 'inbox.html', {
        'chats': chats
    })

@login_required
def message_detail(request, pk):
    chat = Chat.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.created_by = request.user
            chat_message.save()

            chat.save()

            return redirect('chat:detail', pk=pk)
    else:
        form = MessageForm()

    return render(request, 'detail.html', {
        'chat': chat,
        'form': form
    })