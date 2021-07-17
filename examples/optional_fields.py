from typing import Optional

import streamlit as st
from pydantic import BaseModel, Field

import streamlit_pydantic as sp


class ExampleModel(BaseModel):
    some_text: str
    some_number: int
    some_boolean: bool
    optional_boolean: bool = False
    optional_text: Optional[str]
    optional_number: int = Field(20)


data = sp.pydantic_form(
    key="my_form", input_class=ExampleModel, group_optional_fields="expander"
)
if data:
    st.json(data.json())
