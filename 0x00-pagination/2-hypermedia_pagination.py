#!/usr/bin/env python3
"""
This module contains the Server class for paginating a dataset with hypermedia.
"""

import csv
import math
from typing import List, Dict, Optional

Server = __import__('1-simple_pagination').Server


class Server(Server):
    """Server class to paginate a database of popular baby names with hypermedia."""

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Optional[int]]:
        """
        Returns a dictionary containing pagination information.

        Args:
            page (int): The current page number.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing pagination information.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }

