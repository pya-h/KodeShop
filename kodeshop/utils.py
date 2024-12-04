from decouple import config
from django.core.handlers.wsgi import WSGIRequest
from typing import Type
from django.db import models
from math import ceil


class PaginationParams:
    maxItemsInPage = int(config('MAX_ITEMS_IN_PAGE', cast=int, default=30))
    maxButtonsRange = int(config('MAX_PAGINATION_BUTTON_RANGE', cast=int, default=3))

    def __init__(self, request: WSGIRequest, model: Type[models.Model], filters: models.Q | None = None):
        self.model = model
        self.filters = filters
        try:
            self.page = int(request.GET.get('page', 1))
            if self.page < 1:
                raise ValueError('page not positive!')
        except ValueError:
            self.page = 1
        try:
            self.items_count = int(request.GET.get('items', PaginationParams.maxItemsInPage))
            if self.items_count < 1:
                raise ValueError('limit not positive!')
        except ValueError:
            self.items_count = PaginationParams.maxItemsInPage
        self.page_count: int | None = None  # to be calculated while get
        self.total_items_count: int | None = None

    def get_items(self, order_by: str = 'id', order_descending: bool = False):
        if not order_by:
            order_by = 'id'
        if order_descending:
            order_by = f'-{order_by}' if order_by[0] != '-' else order_by
        self.total_items_count = self.model.objects.count()
        self.page_count = ceil(self.total_items_count / self.items_count)
        if self.page > self.page_count:
            self.page = self.page_count
        return (self.model.objects.filter(self.filters) if self.filters else self.model.objects.all()).order_by(order_by)[
                (self.page - 1) * self.items_count:self.page * self.items_count
        ] if self.total_items_count else []

    @property
    def items_limit(self):
        if self.total_items_count is None:
            self.get_items()
        return min(self.items_count, self.total_items_count)