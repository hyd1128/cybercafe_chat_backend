#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from fastapi_pagination import paginate, set_page, set_params
from fastapi_pagination.default import Page, Params

set_page(Page[int])
set_params(Params(page=2, size=10))

page = paginate([*range(100)])
print(page.model_dump_json(indent=4))


