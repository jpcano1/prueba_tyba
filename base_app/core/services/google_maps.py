import os
from typing import Any

import googlemaps

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")


def get_restaurants(
    location: dict[str, float],
    radius: int = 200,
    open_now: bool = False,
) -> list[dict[str, Any]]:
    """
    Retrieve a list of nearby locations.

    :param location: The location in format latitude, longitude
    :param radius: The radius of the search
    :param open_now: A flag to indicate whether
    the restaurants are open or not
    :return: All the restaurants retrieved
    """
    map_client = googlemaps.Client(API_KEY)

    result = map_client.places_nearby(
        location=f"{location['lat']},{location['lng']}",
        type="restaurant",
        open_now=open_now,
        radius=radius,
    )
    return [
        {"name": restaurant["name"], "location": restaurant["geometry"]["location"]}
        for restaurant in result["results"]
    ]
