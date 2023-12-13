#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2020 Cezar H. <https://github.com/usernein>
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.

import pyrogram

from typing import Optional
from pyrogram.types import ListenerTypes, Identifier, Listener

class GetListenerMatchingWithIdentifierPattern:
    def get_listener_matching_with_identifier_pattern(
        self: "pyrogram.Client",
        pattern: Identifier,
        listener_type: ListenerTypes
    ) -> Optional[Listener]:
        """
        Gets a listener that matches the given identifier pattern.

        The difference from :meth:`pyromod.types.Client.get_listener_matching_with_data` is that this method
        intends to get a listener by passing partial info of the listener identifier, while the other method
        intends to get a listener by passing the full info of the update data, which the listener should match with.

        :param pattern: A :class:`pyromod.types.Identifier` to match against.
        :param listener_type: The type of listener to get. Must be a value from :class:`pyromod.types.ListenerTypes`.
        :return: The listener that matches the given identifier pattern or ``None`` if no listener matches.
        """
        matching = []
        for listener in self.listeners[listener_type]:
            if pattern.matches(listener.identifier):
                matching.append(listener)

        # in case of multiple matching listeners, the most specific should be returned

        def count_populated_attributes(listener_item: Listener):
            return listener_item.identifier.count_populated()

        return max(matching, key=count_populated_attributes, default=None)
