# ManagedDefense

## VulnerabilityDiscovery

### Repositories

Types:

```python
from cloudflare.types.managed_defense.vulnerability_discovery import (
    RepositoryCreateResponse,
    RepositoryListResponse,
    RepositoryGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/managed-defense/vulnerability-discovery/repos">client.managed_defense.vulnerability_discovery.repositories.<a href="./src/cloudflare/resources/managed_defense/vulnerability_discovery/repositories.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/managed_defense/vulnerability_discovery/repository_create_params.py">params</a>) -> <a href="./src/cloudflare/types/managed_defense/vulnerability_discovery/repository_create_response.py">RepositoryCreateResponse</a></code>
- <code title="get /accounts/{account_id}/managed-defense/vulnerability-discovery/repos">client.managed_defense.vulnerability_discovery.repositories.<a href="./src/cloudflare/resources/managed_defense/vulnerability_discovery/repositories.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/managed_defense/vulnerability_discovery/repository_list_params.py">params</a>) -> <a href="./src/cloudflare/types/managed_defense/vulnerability_discovery/repository_list_response.py">SyncCursorLimitPagination[RepositoryListResponse]</a></code>
- <code title="get /accounts/{account_id}/managed-defense/vulnerability-discovery/repos/{repo_id}">client.managed_defense.vulnerability_discovery.repositories.<a href="./src/cloudflare/resources/managed_defense/vulnerability_discovery/repositories.py">get</a>(repo_id, \*, account_id, \*\*<a href="src/cloudflare/types/managed_defense/vulnerability_discovery/repository_get_params.py">params</a>) -> <a href="./src/cloudflare/types/managed_defense/vulnerability_discovery/repository_get_response.py">RepositoryGetResponse</a></code>

### Scans

Types:

```python
from cloudflare.types.managed_defense.vulnerability_discovery import (
    ScanCreateResponse,
    ScanListResponse,
    ScanGetResponse,
    ScanGetReportResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/managed-defense/vulnerability-discovery/scans">client.managed_defense.vulnerability_discovery.scans.<a href="./src/cloudflare/resources/managed_defense/vulnerability_discovery/scans.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/managed_defense/vulnerability_discovery/scan_create_params.py">params</a>) -> <a href="./src/cloudflare/types/managed_defense/vulnerability_discovery/scan_create_response.py">ScanCreateResponse</a></code>
- <code title="get /accounts/{account_id}/managed-defense/vulnerability-discovery/scans">client.managed_defense.vulnerability_discovery.scans.<a href="./src/cloudflare/resources/managed_defense/vulnerability_discovery/scans.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/managed_defense/vulnerability_discovery/scan_list_params.py">params</a>) -> <a href="./src/cloudflare/types/managed_defense/vulnerability_discovery/scan_list_response.py">SyncCursorLimitPagination[ScanListResponse]</a></code>
- <code title="get /accounts/{account_id}/managed-defense/vulnerability-discovery/scans/{scan_id}">client.managed_defense.vulnerability_discovery.scans.<a href="./src/cloudflare/resources/managed_defense/vulnerability_discovery/scans.py">get</a>(scan_id, \*, account_id) -> <a href="./src/cloudflare/types/managed_defense/vulnerability_discovery/scan_get_response.py">ScanGetResponse</a></code>
- <code title="get /accounts/{account_id}/managed-defense/vulnerability-discovery/scans/{scan_id}/report">client.managed_defense.vulnerability_discovery.scans.<a href="./src/cloudflare/resources/managed_defense/vulnerability_discovery/scans.py">get_report</a>(scan_id, \*, account_id) -> <a href="./src/cloudflare/types/managed_defense/vulnerability_discovery/scan_get_report_response.py">ScanGetReportResponse</a></code>

### Reports

Types:

```python
from cloudflare.types.managed_defense.vulnerability_discovery import ReportGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/managed-defense/vulnerability-discovery/repos/{repo_id}/scans/{scan_id}/report">client.managed_defense.vulnerability_discovery.reports.<a href="./src/cloudflare/resources/managed_defense/vulnerability_discovery/reports.py">get</a>(scan_id, \*, account_id, repo_id) -> <a href="./src/cloudflare/types/managed_defense/vulnerability_discovery/report_get_response.py">ReportGetResponse</a></code>
