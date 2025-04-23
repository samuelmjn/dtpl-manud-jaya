from datetime import datetime, timezone

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ReviewForm
from .models import Review


def review_form(request, review_token):
    review = get_object_or_404(Review, token=review_token)
    is_expired = datetime.now(timezone.utc) > review.expired_at

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid() and not (review.is_used or is_expired):
            form.save()
            context = {
                'message': 'Terima Kasih atas Ulasan Anda!',
                'review': review
            }
            return render(request, 'review/review_success.html', context)
    else:
        form = ReviewForm()

    if review.is_used:
        context = {
            'error': 'Ulasan sudah pernah diisi',
            'review': review,
        }
        return render(request, 'review/review_error.html', context)

    if is_expired:
        context = {
            'error': 'Link untuk Ulasan sudah kadaluarsa',
            'review': review,
        }
        return render(request, 'review/review_error.html', context)

    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'review/review_form.html', context)