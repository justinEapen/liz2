# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Mental Health Well-Being App! 👋")

    st.sidebar.success("Select your Chatbot Mode")

    st.markdown(
        """
        Ever feel like you're on a rollercoaster of emotions? You're not alone! 
        Mental health is just as important as physical health, and Oasis is here 
        to guide you on your journey to feeling your best.
        ### 👈 Checkout our Chatbot!
        Feeling overwhelmed? Sometimes talking things out can make a big difference. 
        Kirti, our friendly AI chatbot, is here to listen without judgement and offer support 24/7.

        **Made By:**
        - Abinaya A
        - Justin Eapen George
        - Priyanka S
        - Sandra V Yebu
    """
    )


if __name__ == "__main__":
    run()
