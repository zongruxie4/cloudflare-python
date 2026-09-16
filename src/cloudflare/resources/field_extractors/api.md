# FieldExtractors

Types:

```python
from cloudflare.types.field_extractors import (
    FieldExtractorUpdateResponse,
    FieldExtractorGetResponse,
)
```

Methods:

- <code title="put /accounts/{account_id}/field_extractors/{extractor}">client.field_extractors.<a href="./src/cloudflare/resources/field_extractors/field_extractors.py">update</a>(extractor, \*, account_id, \*\*<a href="src/cloudflare/types/field_extractors/field_extractor_update_params.py">params</a>) -> <a href="./src/cloudflare/types/field_extractors/field_extractor_update_response.py">FieldExtractorUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/field_extractors/{extractor}">client.field_extractors.<a href="./src/cloudflare/resources/field_extractors/field_extractors.py">delete</a>(extractor, \*, account_id) -> object</code>
- <code title="get /accounts/{account_id}/field_extractors/{extractor}">client.field_extractors.<a href="./src/cloudflare/resources/field_extractors/field_extractors.py">get</a>(extractor, \*, account_id) -> <a href="./src/cloudflare/types/field_extractors/field_extractor_get_response.py">FieldExtractorGetResponse</a></code>
