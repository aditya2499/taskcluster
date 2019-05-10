# coding=utf-8
#####################################################
# THIS FILE IS AUTOMATICALLY GENERATED. DO NOT EDIT #
#####################################################
# noqa: E128,E201
from .client import BaseClient
from .client import createApiClient
from .client import config
from .client import createTemporaryCredentials
from .client import createSession
_defaultConfig = config


class Auth(BaseClient):
    """
    Authentication related API end-points for Taskcluster and related
    services. These API end-points are of interest if you wish to:
      * Authorize a request signed with Taskcluster credentials,
      * Manage clients and roles,
      * Inspect or audit clients and roles,
      * Gain access to various services guarded by this API.

    Note that in this service "authentication" refers to validating the
    correctness of the supplied credentials (that the caller posesses the
    appropriate access token). This service does not provide any kind of user
    authentication (identifying a particular person).

    ### Clients
    The authentication service manages _clients_, at a high-level each client
    consists of a `clientId`, an `accessToken`, scopes, and some metadata.
    The `clientId` and `accessToken` can be used for authentication when
    calling Taskcluster APIs.

    The client's scopes control the client's access to Taskcluster resources.
    The scopes are *expanded* by substituting roles, as defined below.

    ### Roles
    A _role_ consists of a `roleId`, a set of scopes and a description.
    Each role constitutes a simple _expansion rule_ that says if you have
    the scope: `assume:<roleId>` you get the set of scopes the role has.
    Think of the `assume:<roleId>` as a scope that allows a client to assume
    a role.

    As in scopes the `*` kleene star also have special meaning if it is
    located at the end of a `roleId`. If you have a role with the following
    `roleId`: `my-prefix*`, then any client which has a scope staring with
    `assume:my-prefix` will be allowed to assume the role.

    ### Guarded Services
    The authentication service also has API end-points for delegating access
    to some guarded service such as AWS S3, or Azure Table Storage.
    Generally, we add API end-points to this server when we wish to use
    Taskcluster credentials to grant access to a third-party service used
    by many Taskcluster components.
    """

    classOptions = {
    }
    serviceName = 'auth'
    apiVersion = 'v1'

    def ping(self, *args, **kwargs):
        """
        Ping Server

        Respond without doing anything.
        This endpoint is used to check that the service is up.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["ping"], *args, **kwargs)

    def listClients(self, *args, **kwargs):
        """
        List Clients

        Get a list of all clients.  With `prefix`, only clients for which
        it is a prefix of the clientId are returned.

        By default this end-point will try to return up to 1000 clients in one
        request. But it **may return less, even none**.
        It may also return a `continuationToken` even though there are no more
        results. However, you can only be sure to have seen all results if you
        keep calling `listClients` with the last `continuationToken` until you
        get a result without a `continuationToken`.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["listClients"], *args, **kwargs)

    def client(self, *args, **kwargs):
        """
        Get Client

        Get information about a single client.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["client"], *args, **kwargs)

    def createClient(self, *args, **kwargs):
        """
        Create Client

        Create a new client and get the `accessToken` for this client.
        You should store the `accessToken` from this API call as there is no
        other way to retrieve it.

        If you loose the `accessToken` you can call `resetAccessToken` to reset
        it, and a new `accessToken` will be returned, but you cannot retrieve the
        current `accessToken`.

        If a client with the same `clientId` already exists this operation will
        fail. Use `updateClient` if you wish to update an existing client.

        The caller's scopes must satisfy `scopes`.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["createClient"], *args, **kwargs)

    def resetAccessToken(self, *args, **kwargs):
        """
        Reset `accessToken`

        Reset a clients `accessToken`, this will revoke the existing
        `accessToken`, generate a new `accessToken` and return it from this
        call.

        There is no way to retrieve an existing `accessToken`, so if you loose it
        you must reset the accessToken to acquire it again.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["resetAccessToken"], *args, **kwargs)

    def updateClient(self, *args, **kwargs):
        """
        Update Client

        Update an exisiting client. The `clientId` and `accessToken` cannot be
        updated, but `scopes` can be modified.  The caller's scopes must
        satisfy all scopes being added to the client in the update operation.
        If no scopes are given in the request, the client's scopes remain
        unchanged

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["updateClient"], *args, **kwargs)

    def enableClient(self, *args, **kwargs):
        """
        Enable Client

        Enable a client that was disabled with `disableClient`.  If the client
        is already enabled, this does nothing.

        This is typically used by identity providers to re-enable clients that
        had been disabled when the corresponding identity's scopes changed.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["enableClient"], *args, **kwargs)

    def disableClient(self, *args, **kwargs):
        """
        Disable Client

        Disable a client.  If the client is already disabled, this does nothing.

        This is typically used by identity providers to disable clients when the
        corresponding identity's scopes no longer satisfy the client's scopes.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["disableClient"], *args, **kwargs)

    def deleteClient(self, *args, **kwargs):
        """
        Delete Client

        Delete a client, please note that any roles related to this client must
        be deleted independently.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["deleteClient"], *args, **kwargs)

    def listRoles(self, *args, **kwargs):
        """
        List Roles

        Get a list of all roles, each role object also includes the list of
        scopes it expands to.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["listRoles"], *args, **kwargs)

    def listRoleIds(self, *args, **kwargs):
        """
        List Role IDs

        If no limit is given, the roleIds of all roles are returned. Since this
        list may become long, callers can use the `limit` and `continuationToken`
        query arguments to page through the responses.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["listRoleIds"], *args, **kwargs)

    def listRoles2(self, *args, **kwargs):
        """
        List Roles

        If no limit is given, all roles are returned. Since this
        list may become long, callers can use the `limit` and `continuationToken`
        query arguments to page through the responses.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["listRoles2"], *args, **kwargs)

    def role(self, *args, **kwargs):
        """
        Get Role

        Get information about a single role, including the set of scopes that the
        role expands to.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["role"], *args, **kwargs)

    def createRole(self, *args, **kwargs):
        """
        Create Role

        Create a new role.

        The caller's scopes must satisfy the new role's scopes.

        If there already exists a role with the same `roleId` this operation
        will fail. Use `updateRole` to modify an existing role.

        Creation of a role that will generate an infinite expansion will result
        in an error response.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["createRole"], *args, **kwargs)

    def updateRole(self, *args, **kwargs):
        """
        Update Role

        Update an existing role.

        The caller's scopes must satisfy all of the new scopes being added, but
        need not satisfy all of the role's existing scopes.

        An update of a role that will generate an infinite expansion will result
        in an error response.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["updateRole"], *args, **kwargs)

    def deleteRole(self, *args, **kwargs):
        """
        Delete Role

        Delete a role. This operation will succeed regardless of whether or not
        the role exists.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["deleteRole"], *args, **kwargs)

    def expandScopesGet(self, *args, **kwargs):
        """
        Expand Scopes

        Return an expanded copy of the given scopeset, with scopes implied by any
        roles included.

        This call uses the GET method with an HTTP body.  It remains only for
        backward compatibility.

        This method is ``deprecated``
        """

        return self._makeApiCall(self.funcinfo["expandScopesGet"], *args, **kwargs)

    def expandScopes(self, *args, **kwargs):
        """
        Expand Scopes

        Return an expanded copy of the given scopeset, with scopes implied by any
        roles included.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["expandScopes"], *args, **kwargs)

    def currentScopes(self, *args, **kwargs):
        """
        Get Current Scopes

        Return the expanded scopes available in the request, taking into account all sources
        of scopes and scope restrictions (temporary credentials, assumeScopes, client scopes,
        and roles).

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["currentScopes"], *args, **kwargs)

    def awsS3Credentials(self, *args, **kwargs):
        """
        Get Temporary Read/Write Credentials S3

        Get temporary AWS credentials for `read-write` or `read-only` access to
        a given `bucket` and `prefix` within that bucket.
        The `level` parameter can be `read-write` or `read-only` and determines
        which type of credentials are returned. Please note that the `level`
        parameter is required in the scope guarding access.  The bucket name must
        not contain `.`, as recommended by Amazon.

        This method can only allow access to a whitelisted set of buckets.  To add
        a bucket to that whitelist, contact the Taskcluster team, who will add it to
        the appropriate IAM policy.  If the bucket is in a different AWS account, you
        will also need to add a bucket policy allowing access from the Taskcluster
        account.  That policy should look like this:

        ```
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "allow-taskcluster-auth-to-delegate-access",
              "Effect": "Allow",
              "Principal": {
                "AWS": "arn:aws:iam::692406183521:root"
              },
              "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:GetBucketLocation"
              ],
              "Resource": [
                "arn:aws:s3:::<bucket>",
                "arn:aws:s3:::<bucket>/*"
              ]
            }
          ]
        }
        ```

        The credentials are set to expire after an hour, but this behavior is
        subject to change. Hence, you should always read the `expires` property
        from the response, if you intend to maintain active credentials in your
        application.

        Please note that your `prefix` may not start with slash `/`. Such a prefix
        is allowed on S3, but we forbid it here to discourage bad behavior.

        Also note that if your `prefix` doesn't end in a slash `/`, the STS
        credentials may allow access to unexpected keys, as S3 does not treat
        slashes specially.  For example, a prefix of `my-folder` will allow
        access to `my-folder/file.txt` as expected, but also to `my-folder.txt`,
        which may not be intended.

        Finally, note that the `PutObjectAcl` call is not allowed.  Passing a canned
        ACL other than `private` to `PutObject` is treated as a `PutObjectAcl` call, and
        will result in an access-denied error from AWS.  This limitation is due to a
        security flaw in Amazon S3 which might otherwise allow indefinite access to
        uploaded objects.

        **EC2 metadata compatibility**, if the querystring parameter
        `?format=iam-role-compat` is given, the response will be compatible
        with the JSON exposed by the EC2 metadata service. This aims to ease
        compatibility for libraries and tools built to auto-refresh credentials.
        For details on the format returned by EC2 metadata service see:
        [EC2 User Guide](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#instance-metadata-security-credentials).

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["awsS3Credentials"], *args, **kwargs)

    def azureAccounts(self, *args, **kwargs):
        """
        List Accounts Managed by Auth

        Retrieve a list of all Azure accounts managed by Taskcluster Auth.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["azureAccounts"], *args, **kwargs)

    def azureTables(self, *args, **kwargs):
        """
        List Tables in an Account Managed by Auth

        Retrieve a list of all tables in an account.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["azureTables"], *args, **kwargs)

    def azureTableSAS(self, *args, **kwargs):
        """
        Get Shared-Access-Signature for Azure Table

        Get a shared access signature (SAS) string for use with a specific Azure
        Table Storage table.

        The `level` parameter can be `read-write` or `read-only` and determines
        which type of credentials are returned.  If level is read-write, it will create the
        table if it doesn't already exist.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["azureTableSAS"], *args, **kwargs)

    def azureContainers(self, *args, **kwargs):
        """
        List containers in an Account Managed by Auth

        Retrieve a list of all containers in an account.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["azureContainers"], *args, **kwargs)

    def azureContainerSAS(self, *args, **kwargs):
        """
        Get Shared-Access-Signature for Azure Container

        Get a shared access signature (SAS) string for use with a specific Azure
        Blob Storage container.

        The `level` parameter can be `read-write` or `read-only` and determines
        which type of credentials are returned.  If level is read-write, it will create the
        container if it doesn't already exist.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["azureContainerSAS"], *args, **kwargs)

    def sentryDSN(self, *args, **kwargs):
        """
        Get DSN for Sentry Project

        Get temporary DSN (access credentials) for a sentry project.
        The credentials returned can be used with any Sentry client for up to
        24 hours, after which the credentials will be automatically disabled.

        If the project doesn't exist it will be created, and assigned to the
        initial team configured for this component. Contact a Sentry admin
        to have the project transferred to a team you have access to if needed

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["sentryDSN"], *args, **kwargs)

    def statsumToken(self, *args, **kwargs):
        """
        Get Token for Statsum Project

        Get temporary `token` and `baseUrl` for sending metrics to statsum.

        The token is valid for 24 hours, clients should refresh after expiration.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["statsumToken"], *args, **kwargs)

    def websocktunnelToken(self, *args, **kwargs):
        """
        Get a client token for the Websocktunnel service

        Get a temporary token suitable for use connecting to a
        [websocktunnel](https://github.com/taskcluster/websocktunnel) server.

        The resulting token will only be accepted by servers with a matching audience
        value.  Reaching such a server is the callers responsibility.  In general,
        a server URL or set of URLs should be provided to the caller as configuration
        along with the audience value.

        The token is valid for a limited time (on the scale of hours). Callers should
        refresh it before expiration.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["websocktunnelToken"], *args, **kwargs)

    def authenticateHawk(self, *args, **kwargs):
        """
        Authenticate Hawk Request

        Validate the request signature given on input and return list of scopes
        that the authenticating client has.

        This method is used by other services that wish rely on Taskcluster
        credentials for authentication. This way we can use Hawk without having
        the secret credentials leave this service.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["authenticateHawk"], *args, **kwargs)

    def testAuthenticate(self, *args, **kwargs):
        """
        Test Authentication

        Utility method to test client implementations of Taskcluster
        authentication.

        Rather than using real credentials, this endpoint accepts requests with
        clientId `tester` and accessToken `no-secret`. That client's scopes are
        based on `clientScopes` in the request body.

        The request is validated, with any certificate, authorizedScopes, etc.
        applied, and the resulting scopes are checked against `requiredScopes`
        from the request body. On success, the response contains the clientId
        and scopes as seen by the API method.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["testAuthenticate"], *args, **kwargs)

    def testAuthenticateGet(self, *args, **kwargs):
        """
        Test Authentication (GET)

        Utility method similar to `testAuthenticate`, but with the GET method,
        so it can be used with signed URLs (bewits).

        Rather than using real credentials, this endpoint accepts requests with
        clientId `tester` and accessToken `no-secret`. That client's scopes are
        `['test:*', 'auth:create-client:test:*']`.  The call fails if the
        `test:authenticate-get` scope is not available.

        The request is validated, with any certificate, authorizedScopes, etc.
        applied, and the resulting scopes are checked, just like any API call.
        On success, the response contains the clientId and scopes as seen by
        the API method.

        This method may later be extended to allow specification of client and
        required scopes via query arguments.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["testAuthenticateGet"], *args, **kwargs)

    funcinfo = {
        "authenticateHawk": {
            'args': [],
            'method': 'post',
            'name': 'authenticateHawk',
            'route': '/authenticate-hawk',
            'stability': 'stable',
        },
        "awsS3Credentials": {
            'args': ['level', 'bucket', 'prefix'],
            'method': 'get',
            'name': 'awsS3Credentials',
            'query': ['format'],
            'route': '/aws/s3/<level>/<bucket>/<prefix>',
            'stability': 'stable',
        },
        "azureAccounts": {
            'args': [],
            'method': 'get',
            'name': 'azureAccounts',
            'route': '/azure/accounts',
            'stability': 'stable',
        },
        "azureContainerSAS": {
            'args': ['account', 'container', 'level'],
            'method': 'get',
            'name': 'azureContainerSAS',
            'route': '/azure/<account>/containers/<container>/<level>',
            'stability': 'stable',
        },
        "azureContainers": {
            'args': ['account'],
            'method': 'get',
            'name': 'azureContainers',
            'query': ['continuationToken'],
            'route': '/azure/<account>/containers',
            'stability': 'stable',
        },
        "azureTableSAS": {
            'args': ['account', 'table', 'level'],
            'method': 'get',
            'name': 'azureTableSAS',
            'route': '/azure/<account>/table/<table>/<level>',
            'stability': 'stable',
        },
        "azureTables": {
            'args': ['account'],
            'method': 'get',
            'name': 'azureTables',
            'query': ['continuationToken'],
            'route': '/azure/<account>/tables',
            'stability': 'stable',
        },
        "client": {
            'args': ['clientId'],
            'method': 'get',
            'name': 'client',
            'route': '/clients/<clientId>',
            'stability': 'stable',
        },
        "createClient": {
            'args': ['clientId'],
            'method': 'put',
            'name': 'createClient',
            'route': '/clients/<clientId>',
            'stability': 'stable',
        },
        "createRole": {
            'args': ['roleId'],
            'method': 'put',
            'name': 'createRole',
            'route': '/roles/<roleId>',
            'stability': 'stable',
        },
        "currentScopes": {
            'args': [],
            'method': 'get',
            'name': 'currentScopes',
            'route': '/scopes/current',
            'stability': 'stable',
        },
        "deleteClient": {
            'args': ['clientId'],
            'method': 'delete',
            'name': 'deleteClient',
            'route': '/clients/<clientId>',
            'stability': 'stable',
        },
        "deleteRole": {
            'args': ['roleId'],
            'method': 'delete',
            'name': 'deleteRole',
            'route': '/roles/<roleId>',
            'stability': 'stable',
        },
        "disableClient": {
            'args': ['clientId'],
            'method': 'post',
            'name': 'disableClient',
            'route': '/clients/<clientId>/disable',
            'stability': 'stable',
        },
        "enableClient": {
            'args': ['clientId'],
            'method': 'post',
            'name': 'enableClient',
            'route': '/clients/<clientId>/enable',
            'stability': 'stable',
        },
        "expandScopes": {
            'args': [],
            'method': 'post',
            'name': 'expandScopes',
            'route': '/scopes/expand',
            'stability': 'stable',
        },
        "expandScopesGet": {
            'args': [],
            'method': 'get',
            'name': 'expandScopesGet',
            'route': '/scopes/expand',
            'stability': 'deprecated',
        },
        "listClients": {
            'args': [],
            'method': 'get',
            'name': 'listClients',
            'query': ['prefix', 'continuationToken', 'limit'],
            'route': '/clients/',
            'stability': 'stable',
        },
        "listRoleIds": {
            'args': [],
            'method': 'get',
            'name': 'listRoleIds',
            'query': ['continuationToken', 'limit'],
            'route': '/roleids/',
            'stability': 'stable',
        },
        "listRoles": {
            'args': [],
            'method': 'get',
            'name': 'listRoles',
            'route': '/roles/',
            'stability': 'stable',
        },
        "listRoles2": {
            'args': [],
            'method': 'get',
            'name': 'listRoles2',
            'query': ['continuationToken', 'limit'],
            'route': '/roles2/',
            'stability': 'stable',
        },
        "ping": {
            'args': [],
            'method': 'get',
            'name': 'ping',
            'route': '/ping',
            'stability': 'stable',
        },
        "resetAccessToken": {
            'args': ['clientId'],
            'method': 'post',
            'name': 'resetAccessToken',
            'route': '/clients/<clientId>/reset',
            'stability': 'stable',
        },
        "role": {
            'args': ['roleId'],
            'method': 'get',
            'name': 'role',
            'route': '/roles/<roleId>',
            'stability': 'stable',
        },
        "sentryDSN": {
            'args': ['project'],
            'method': 'get',
            'name': 'sentryDSN',
            'route': '/sentry/<project>/dsn',
            'stability': 'stable',
        },
        "statsumToken": {
            'args': ['project'],
            'method': 'get',
            'name': 'statsumToken',
            'route': '/statsum/<project>/token',
            'stability': 'stable',
        },
        "testAuthenticate": {
            'args': [],
            'method': 'post',
            'name': 'testAuthenticate',
            'route': '/test-authenticate',
            'stability': 'stable',
        },
        "testAuthenticateGet": {
            'args': [],
            'method': 'get',
            'name': 'testAuthenticateGet',
            'route': '/test-authenticate-get/',
            'stability': 'stable',
        },
        "updateClient": {
            'args': ['clientId'],
            'method': 'post',
            'name': 'updateClient',
            'route': '/clients/<clientId>',
            'stability': 'stable',
        },
        "updateRole": {
            'args': ['roleId'],
            'method': 'post',
            'name': 'updateRole',
            'route': '/roles/<roleId>',
            'stability': 'stable',
        },
        "websocktunnelToken": {
            'args': ['wstAudience', 'wstClient'],
            'method': 'get',
            'name': 'websocktunnelToken',
            'route': '/websocktunnel/<wstAudience>/<wstClient>',
            'stability': 'stable',
        },
    }


__all__ = ['createTemporaryCredentials', 'config', '_defaultConfig', 'createApiClient', 'createSession', 'Auth']
