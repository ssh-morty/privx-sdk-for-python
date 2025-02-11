from http import HTTPStatus
from typing import Optional

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse
from privx_api.utils import get_value


class AuthAPI(BasePrivXAPI):
    """
    PrivX Authentication API
    """

    def authenticate(self, username: str, password: str):
        """
        Login api client to the API.

        Raises:
            An InternalAPIException on failure
        """
        # TODO: should return PrivXAPIResponse
        self._authenticate(username, password)

    def get_auth_service_status(self) -> PrivXAPIResponse:
        """
        Get microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.AUTH.STATUS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_idp_client(self, idp_id: str) -> PrivXAPIResponse:
        """
        Get existing identity provider client configuration.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.AUTH.IDP_CLIENT,
            path_params={"idp_id": idp_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_idp_client(self, idp_client: dict) -> PrivXAPIResponse:
        """
        Create an IDP client

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.AUTH.IDP_CLIENTS, body=idp_client
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def update_idp_client(self, idp_id: str, idp_client: dict) -> PrivXAPIResponse:
        """
        Update an IDP client, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.AUTH.IDP_CLIENT, path_params={"idp_id": idp_id}, body=idp_client
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_idp_client(self, idp_id: str) -> PrivXAPIResponse:
        """
        Delete IDP client

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.AUTH.IDP_CLIENT, path_params={"idp_id": idp_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def regenerate_idp_client_config(self, idp_id: str) -> PrivXAPIResponse:
        """
        Create a new identity provider configuration.
        client_id and client_secret are automatically generated by server.

        Returns:
            PrivXAPIResponse:
        """
        response_status, data = self._http_post(
            UrlEnum.AUTH.REGENERATE_IDP_CLIENT, path_params={"idp_id": idp_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_user_sessions(
        self,
        user_id: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Fetch valid sessions for the user.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.AUTH.USER_SESSIONS,
            path_params={"user_id": user_id},
        )
        print(response_status, data)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_source_sessions(
        self,
        source_id: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Fetch valid source sessions.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.AUTH.SOURCE_SESSIONS,
            path_params={"source_id": source_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_sessions(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        search_payload: Optional[dict] = None,
    ) -> PrivXAPIResponse:
        """
        Search for sessions.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sort_key, sortdir=sort_dir
        )

        response_status, data = self._http_post(
            UrlEnum.AUTH.SEARCH_SESSIONS,
            query_params=search_params,
            body=get_value(search_payload, dict()),
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def terminate_session(self, session_id: str) -> PrivXAPIResponse:
        """
        Terminate single session by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.AUTH.TERMINATE_SESSION,
            path_params={"session_id": session_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def terminate_user_sessions(self, user_id: str) -> PrivXAPIResponse:
        """
        Terminate all sessions for a user.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.AUTH.TERMINATE_USER_SESSIONS,
            path_params={"user_id": user_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def logout(self) -> PrivXAPIResponse:
        """
        User logout.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(UrlEnum.AUTH.LOGOUT)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
