# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.query_encoder import encode_query
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from .types.document_metadata_patch import DocumentMetadataPatch
from .types.upload_document_response import UploadDocumentResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DocumentCatalogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def upload_document_contents(
        self,
        *,
        document_name: str,
        document_contents: str,
        allowed_users_email_addresses: typing.Sequence[str],
        upload_as_user_email: str,
        document_external_id: str,
        document_external_url: typing.Optional[str] = OMIT,
        custom_metadata: typing.Optional[typing.Any] = OMIT,
        collection_id: typing.Optional[str] = OMIT,
        force_update: typing.Optional[bool] = OMIT,
        internal_public: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadDocumentResponse:
        """
        Parameters
        ----------
        document_name : str
            The name of the document you want to upload.


        document_contents : str
            The full LLM-formatted text contents of the document you want to upload.


        allowed_users_email_addresses : typing.Sequence[str]
            Users allowed to access the document. Unlike Credal's out of the box connectors which reconcile various permissions models from 3rd party software, for custom uploads the caller is responsible for specifying who can access the document and currently flattening groups if applicable. Documents can also be marked as internal public.


        upload_as_user_email : str
            [Legacy] The user on behalf of whom the document should be uploaded. In most cases, this can simply be the email of the developer making the API call. This field will be removed in the future in favor of purely specifying permissions via allowedUsersEmailAddresses.


        document_external_id : str
            The external ID of the document. This is typically the ID as it exists in its original external system. Uploads to the same external ID will update the document in Credal.


        document_external_url : typing.Optional[str]
            The external URL of the document you want to upload. If provided Credal will link to this URL.


        custom_metadata : typing.Optional[typing.Any]
            Optional JSON representing any custom metdata for this document


        collection_id : typing.Optional[str]
            If specified, document will also be added to a particular document collection


        force_update : typing.Optional[bool]
            If specified, document contents will be re-uploaded and re-embedded even if the document already exists in Credal


        internal_public : typing.Optional[bool]
            If specified, document will be accessible to everyone within the organization of the uploader


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadDocumentResponse

        Examples
        --------
        from credal.client import CredalApi

        client = CredalApi(
            api_key="YOUR_API_KEY",
        )
        client.document_catalog.upload_document_contents(
            document_name="My Document",
            document_contents="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            document_external_id="73eead26-d124-4940-b329-5f068a0a8db9",
            allowed_users_email_addresses=["jack@credal.ai", "ravin@credal.ai"],
            upload_as_user_email="jack@credal.ai",
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "documentName": document_name,
            "documentContents": document_contents,
            "allowedUsersEmailAddresses": allowed_users_email_addresses,
            "uploadAsUserEmail": upload_as_user_email,
            "documentExternalId": document_external_id,
        }
        if document_external_url is not OMIT:
            _request["documentExternalUrl"] = document_external_url
        if custom_metadata is not OMIT:
            _request["customMetadata"] = custom_metadata
        if collection_id is not OMIT:
            _request["collectionId"] = collection_id
        if force_update is not OMIT:
            _request["forceUpdate"] = force_update
        if internal_public is not OMIT:
            _request["internalPublic"] = internal_public
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v0/catalog/uploadDocumentContents"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(UploadDocumentResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def metadata(
        self,
        *,
        sources: typing.Sequence[DocumentMetadataPatch],
        upload_as_user_email: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Bulk patch metadata for documents, synced natively by Credal or manual API uploads

        Parameters
        ----------
        sources : typing.Sequence[DocumentMetadataPatch]

        upload_as_user_email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from credal import DocumentMetadataPatch, ResourceIdentifier_ExternalResourceId
        from credal.client import CredalApi

        client = CredalApi(
            api_key="YOUR_API_KEY",
        )
        client.document_catalog.metadata(
            sources=[
                DocumentMetadataPatch(
                    metadata={"Department": "HR", "Country": "United States"},
                    resource_identifier=ResourceIdentifier_ExternalResourceId(
                        external_resource_id="170NrBm0Do7gdzvr54UvyslPVWkQFOA0lgNycFmdZJQr",
                        resource_type="GOOGLE_DRIVE_ITEM",
                    ),
                ),
                DocumentMetadataPatch(
                    metadata={"Department": "Sales", "Vertical": "Healthcare"},
                    resource_identifier=ResourceIdentifier_ExternalResourceId(
                        external_resource_id="123456",
                        resource_type="ZENDESK_TICKET",
                    ),
                ),
            ],
            upload_as_user_email="ben@credal.ai",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"sources": sources, "uploadAsUserEmail": upload_as_user_email}
        _response = self._client_wrapper.httpx_client.request(
            method="PATCH",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v0/catalog/metadata"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDocumentCatalogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def upload_document_contents(
        self,
        *,
        document_name: str,
        document_contents: str,
        allowed_users_email_addresses: typing.Sequence[str],
        upload_as_user_email: str,
        document_external_id: str,
        document_external_url: typing.Optional[str] = OMIT,
        custom_metadata: typing.Optional[typing.Any] = OMIT,
        collection_id: typing.Optional[str] = OMIT,
        force_update: typing.Optional[bool] = OMIT,
        internal_public: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadDocumentResponse:
        """
        Parameters
        ----------
        document_name : str
            The name of the document you want to upload.


        document_contents : str
            The full LLM-formatted text contents of the document you want to upload.


        allowed_users_email_addresses : typing.Sequence[str]
            Users allowed to access the document. Unlike Credal's out of the box connectors which reconcile various permissions models from 3rd party software, for custom uploads the caller is responsible for specifying who can access the document and currently flattening groups if applicable. Documents can also be marked as internal public.


        upload_as_user_email : str
            [Legacy] The user on behalf of whom the document should be uploaded. In most cases, this can simply be the email of the developer making the API call. This field will be removed in the future in favor of purely specifying permissions via allowedUsersEmailAddresses.


        document_external_id : str
            The external ID of the document. This is typically the ID as it exists in its original external system. Uploads to the same external ID will update the document in Credal.


        document_external_url : typing.Optional[str]
            The external URL of the document you want to upload. If provided Credal will link to this URL.


        custom_metadata : typing.Optional[typing.Any]
            Optional JSON representing any custom metdata for this document


        collection_id : typing.Optional[str]
            If specified, document will also be added to a particular document collection


        force_update : typing.Optional[bool]
            If specified, document contents will be re-uploaded and re-embedded even if the document already exists in Credal


        internal_public : typing.Optional[bool]
            If specified, document will be accessible to everyone within the organization of the uploader


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadDocumentResponse

        Examples
        --------
        from credal.client import AsyncCredalApi

        client = AsyncCredalApi(
            api_key="YOUR_API_KEY",
        )
        await client.document_catalog.upload_document_contents(
            document_name="My Document",
            document_contents="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            document_external_id="73eead26-d124-4940-b329-5f068a0a8db9",
            allowed_users_email_addresses=["jack@credal.ai", "ravin@credal.ai"],
            upload_as_user_email="jack@credal.ai",
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "documentName": document_name,
            "documentContents": document_contents,
            "allowedUsersEmailAddresses": allowed_users_email_addresses,
            "uploadAsUserEmail": upload_as_user_email,
            "documentExternalId": document_external_id,
        }
        if document_external_url is not OMIT:
            _request["documentExternalUrl"] = document_external_url
        if custom_metadata is not OMIT:
            _request["customMetadata"] = custom_metadata
        if collection_id is not OMIT:
            _request["collectionId"] = collection_id
        if force_update is not OMIT:
            _request["forceUpdate"] = force_update
        if internal_public is not OMIT:
            _request["internalPublic"] = internal_public
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v0/catalog/uploadDocumentContents"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(UploadDocumentResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def metadata(
        self,
        *,
        sources: typing.Sequence[DocumentMetadataPatch],
        upload_as_user_email: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Bulk patch metadata for documents, synced natively by Credal or manual API uploads

        Parameters
        ----------
        sources : typing.Sequence[DocumentMetadataPatch]

        upload_as_user_email : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from credal import DocumentMetadataPatch, ResourceIdentifier_ExternalResourceId
        from credal.client import AsyncCredalApi

        client = AsyncCredalApi(
            api_key="YOUR_API_KEY",
        )
        await client.document_catalog.metadata(
            sources=[
                DocumentMetadataPatch(
                    metadata={"Department": "HR", "Country": "United States"},
                    resource_identifier=ResourceIdentifier_ExternalResourceId(
                        external_resource_id="170NrBm0Do7gdzvr54UvyslPVWkQFOA0lgNycFmdZJQr",
                        resource_type="GOOGLE_DRIVE_ITEM",
                    ),
                ),
                DocumentMetadataPatch(
                    metadata={"Department": "Sales", "Vertical": "Healthcare"},
                    resource_identifier=ResourceIdentifier_ExternalResourceId(
                        external_resource_id="123456",
                        resource_type="ZENDESK_TICKET",
                    ),
                ),
            ],
            upload_as_user_email="ben@credal.ai",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"sources": sources, "uploadAsUserEmail": upload_as_user_email}
        _response = await self._client_wrapper.httpx_client.request(
            method="PATCH",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v0/catalog/metadata"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
