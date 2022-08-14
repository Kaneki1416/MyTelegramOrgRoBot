#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Shrimadhav U K
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


class Translation:
    START_TEXT = (
        " 🍽️ Hi!\n"
        " 🤝 Thank you for using me 😬\n"
        ". ☎️ Enter your number along with the country code: "
           " 📞 Example : +1452677888 "
          )
    AFTER_RECVD_CODE_TEXT = (
        "🕊️ I see!\n"
        " 💠 Enter Code: "
        " 🪴 you received from Telegram!\n\n"      
    )
    BEFORE_SUCC_LOGIN = "🪴 Getting your api please stand by..."
    ERRED_PAGE = "❌ Failed to get api"
    CANCELLED_MESG = "✨ Bye! Please enter your phone number again "
    IN_VALID_CODE_PVDED = (
        "✨ sorry, "
        " 🪴 But the code looks pretty much wrong "
        "  🧪 Use /start and put your number again  "
    )
    IN_VALID_PHNO_PVDED = (
        "🪴 sorry, "
        " ✨ but the phone number seems wrong "
        "  🧪 Put a right number "
    )
