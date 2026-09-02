# Reference
## Metadata
<details><summary><code>client.metadata.<a href="src/alpha/metadata/client.py">get_api_index</a>() -> ApiIndexResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.metadata.get_api_index()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metadata.<a href="src/alpha/metadata/client.py">list_tools</a>() -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the live tool catalog and JSON input schemas used by both the REST API and MCP.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.metadata.list_tools()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Vaults
<details><summary><code>client.vaults.<a href="src/alpha/vaults/client.py">list_vaults</a>() -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the vaults the credential holder may access. If more than one vault is returned, pass the exact vault id to later calls.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.vaults.list_vaults()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Knowledge
<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">suggest_vault_scope</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resolve the minimum safe vault scope from the user's recent conversation, using only this API key holder's authorized vault names, keywords, known people and cached summaries. Call it after list_vaults when the right vault is not explicit. Returns selected vault ids or a focused clarification question; it does not search vault content.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.suggest_vault_scope(
    conversation="conversation",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation:** `str` — The recent user conversation that identifies a client, project, person or topic (maximum 12,000 trailing characters used).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">search_knowledge</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search the discovery knowledge base (departments, people, processes, systems, problems, opportunities, KPIs) by name or alias. Returns matching entities with descriptions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.search_knowledge(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — Name or alias to search for
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[SearchKnowledgeRequestType]` — Optional entity type filter
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">get_entity</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one entity in depth: core fields (description, aliases, recency) plus slim deduped graph edges ({entityId, name, type, relation, direction, weight}. weight = number of co-mentions across meetings). Set includeEvidence=true to also get the verbatim quotes (who said it, in which meeting). A conflicts array appears when the evidence contains contradictory claims needing validation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.get_entity(
    entity_id="entityId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — Entity id from a previous call
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**include_evidence:** `typing.Optional[bool]` — Include verbatim evidence quotes (default false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">search_transcripts</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Semantic search over the meeting transcripts. Returns the most relevant verbatim excerpts with speakers and meeting names.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.search_transcripts(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — What to look for
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">list_meetings</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the discovery meetings (name, date, attendees, extraction status).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.list_meetings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">list_calendar</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Project calendar events, recent (45 days back) and scheduled ahead: title, ISO datetime, a happened flag, attendees, Meet link. Cross with list_meetings (recorded) to distinguish what already happened from what is merely booked.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.list_calendar()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">get_meeting</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one meeting: metadata, notes (markdown), and the entities extracted from it (with per-meeting mention counts). use it to answer 'what came out of meeting X'.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.get_meeting(
    meeting_id="meetingId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**meeting_id:** `str` — Meeting id from list_meetings
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">list_findings</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Paginated findings inventory. Filters: type, source, meetingId (only entities from that meeting). sort: 'mentions' (default) or 'recent' (by lastMentionedAt). compact=true returns only {id, name, type, mentionCount, lastMentionedAt}. recommended for orientation; fetch details with get_entity. Returns {findings, total, nextCursor}.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.list_findings()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListFindingsRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[ListFindingsRequestSource]` 
    
</dd>
</dl>

<dl>
<dd>

**meeting_id:** `typing.Optional[str]` — Only entities with evidence from this meeting
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListFindingsRequestSort]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Page size (default 50, max 200)
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — nextCursor from the previous page
    
</dd>
</dl>

<dl>
<dd>

**compact:** `typing.Optional[bool]` — Slim payload (default false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">list_tasks</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Action-plan tasks with the full board surface: id (for update_task), board identifier, named owner, t-shirt estimate, priority, labels, checklist, due date and milestone. status "open" = everything not done.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.list_tasks()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListTasksRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**milestone_id:** `typing.Optional[str]` — Only tasks in this milestone (id from list_milestones)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">list_files</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the project's PUBLIC files (name, description, download URL). Internal files are never served here. Give the URL to the user as a link when they ask for a file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.list_files()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">get_file</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one PUBLIC file: metadata, a temporary download URL, and a content excerpt when the file was parsed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.get_file(
    file_id="fileId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — File id from list_files
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">list_plan_steps</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The mutual action plan timeline (macro project steps, status, and whether each was proposed by the agent or a person).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.list_plan_steps()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">changes_since</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

What's new since a given moment: entities first seen after it, entities re-mentioned after it, and new meetings. The natural 'what changed since we last talked' call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.changes_since(
    since="since",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**since:** `str` — ISO 8601 datetime, e.g. 2026-07-18T00:00:00Z
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">stats</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cheap orientation: entity counts by type, meetings extracted/total, tasks by status. Call this first to size the knowledge base.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.stats()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">get_brief</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The latest agent-written brief. kind 'daily' (default) is the current 'what's going on' snapshot of the vault; 'weekly-plan' and 'weekly-digest' mirror the Monday plan and Friday digest e-mails. Good second call after stats for orientation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.get_brief()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[GetBriefRequestKind]` — Which brief (default daily)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">get_transcript</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read a meeting transcript sequentially in chunks (complements semantic search). Returns {chunks: [{index, speakers, text}], totalChunks, nextOffset}.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.get_transcript(
    meeting_id="meetingId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**meeting_id:** `str` — Meeting id from list_meetings
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[float]` — Chunk offset (default 0)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — Chunks per page (default 20, max 50)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">list_conflicts</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Contradictions detected across the evidence: pairs of credible claims about the same entity that cannot both be true (with speakers and meetings). Default shows open ones needing client validation; filter by status or 'all' to see resolved/dismissed history with notes. Use the id with resolve_conflict.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.list_conflicts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListConflictsRequestStatus]` — Which conflicts (default open)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">list_milestones</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Project milestones with task tallies (id, title, target date, tasks done/total). Use to resolve milestone ids before add_task/update_task, or to answer 'what's left in milestone X'.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.list_milestones()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">find_person</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Look someone up in this vault's people registry: name, e-mail, title, organisation. The ONLY authoritative source for an address. never guess one or assume a pattern like first.last@company.com.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.find_person()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Name, address or role fragment
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">list_sent_emails</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Messages this vault's agent already sent, newest first, with the handles needed to reply INSIDE the same conversation (replyToThreadId, inReplyToMessageId). Pass one back to send_email so a reply threads instead of starting a parallel conversation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.list_sent_emails()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[str]` — Narrow to one recipient
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — 1-25, default 10
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">find_email_thread</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search the vault's connected Gmail for an existing conversation, including mail sent before this deployment started logging. Gmail search syntax, e.g. "to:ana@client.com inventory" or "subject:report newer_than:7d". Returns thread ids for send_email's replyToThreadId.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.find_email_thread(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — Gmail search syntax
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — 1-20, default 5
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">find_artifact</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find a file that already exists in this vault: something the agent generated (chart, workbook, CSV, report) or a document a member added. Search by title, newest first. Use it BEFORE rebuilding anything, and to get the artifactId that send_email attaches.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.find_artifact()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Words from the title. Omit to list the most recent.
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[FindArtifactRequestKind]` — Narrow to one kind of file
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — 1-25, default 10
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">search_agent_memory</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search the agent's OWN past conversations in this vault. e-mail, MCP and portal chat. for what was already asked, answered or decided. This is conversation history, NOT the knowledge base: use search_knowledge or search_transcripts for what was said in meetings.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.search_agent_memory(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — What was talked about
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**person_email:** `typing.Optional[str]` — Narrow to exchanges with one person
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — 1-25, default 12
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/alpha/knowledge/client.py">expand_graph</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Graph traversal from an entity: depth 1 = its slim edges; depth 2 = neighborhood expansion (capped at 120 edges, second-hop relations prefixed with the intermediate node). Use to explore paths between areas.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.knowledge.expand_graph(
    entity_id="entityId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — Starting entity id
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[float]` — 1 or 2 (default 1)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Actions
<details><summary><code>client.actions.<a href="src/alpha/actions/client.py">resolve_conflict</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Close out a contradiction by id (from list_conflicts): status 'resolved' (validated with the client. say what the truth turned out to be in the note) or 'dismissed' (duplicate, transcription noise, not a real conflict. note why). Passing 'open' reopens one. Requires a manager API key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.actions.resolve_conflict(
    conflict_id="conflictId",
    status="resolved",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conflict_id:** `str` — Conflict id from list_conflicts
    
</dd>
</dl>

<dl>
<dd>

**status:** `ResolveConflictRequestStatus` 
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — Resolution note: the validated answer, or why it was dismissed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/alpha/actions/client.py">add_task</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a task on the vault's board. The owner may be a person's name or a company placeholder. Supports the full kanban surface: t-shirt estimate, priority, labels, checklist, due date and milestone (resolve ids with list_milestones). Requires a manager API key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.actions.add_task(
    title="title",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**title:** `str` — Short actionable title (short and actionable)
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional detail
    
</dd>
</dl>

<dl>
<dd>

**assignee_name:** `typing.Optional[str]` — Responsible person or company
    
</dd>
</dl>

<dl>
<dd>

**estimate:** `typing.Optional[AddTaskRequestEstimate]` — T-shirt effort size
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[AddTaskRequestPriority]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**checklist:** `typing.Optional[typing.List[AddTaskRequestChecklistItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[str]` — ISO date, e.g. 2026-08-15
    
</dd>
</dl>

<dl>
<dd>

**milestone_id:** `typing.Optional[str]` — Milestone id from list_milestones
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/alpha/actions/client.py">update_task</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit an existing task by its board identifier (for example 'ACME-5', or just 5; the prefix is whatever this vault uses) or by taskId from list_tasks. Fields: status, named owner, t-shirt estimate, priority, labels, checklist, due date, milestone, title and description. Pass null to clear a clearable field (estimate, dueDate, milestoneId, assigneeName, description). Requires a manager API key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.actions.update_task()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `typing.Optional[UpdateTaskRequestIdentifier]` — Board reference: e.g. 'ACME-5', or just 5
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `typing.Optional[str]` — Task id from list_tasks (alternative to identifier)
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[UpdateTaskRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**assignee_name:** `typing.Optional[str]` — Responsible person or company; null clears it
    
</dd>
</dl>

<dl>
<dd>

**estimate:** `typing.Optional[UpdateTaskRequestEstimate]` — T-shirt effort size; null clears it
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[UpdateTaskRequestPriority]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.List[str]]` — Replaces the label list ([] clears)
    
</dd>
</dl>

<dl>
<dd>

**checklist:** `typing.Optional[typing.List[UpdateTaskRequestChecklistItem]]` — Replaces the checklist ([] clears)
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[str]` — ISO date; null clears
    
</dd>
</dl>

<dl>
<dd>

**milestone_id:** `typing.Optional[str]` — Milestone id from list_milestones; null clears
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/alpha/actions/client.py">send_email</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an e-mail from the vault agent's mailbox to a VAULT MEMBER or registered stakeholder. Can carry files: pass artifact ids from find_artifact. Can also reply INSIDE an existing thread, or be left as a draft in the connected Gmail account for a person to review and send. Requires a manager API key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.actions.send_email(
    to="to",
    subject="subject",
    body="body",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**to:** `str` — Recipient (must belong to this vault)
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `str` — Plain-text body
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**cc:** `typing.Optional[typing.List[str]]` — Copied recipients, subject to the same vault check as `to`
    
</dd>
</dl>

<dl>
<dd>

**attachment_ids:** `typing.Optional[typing.List[str]]` — artifactId values from find_artifact. Files only, never URLs.
    
</dd>
</dl>

<dl>
<dd>

**send_as:** `typing.Optional[SendEmailRequestSendAs]` — 'agent' (default) sends from the vault agent's address and takes several attachments; 'me' sends from the vault's connected Gmail and takes one.
    
</dd>
</dl>

<dl>
<dd>

**reply_to_thread_id:** `typing.Optional[str]` — Gmail thread id, to reply inside an existing conversation
    
</dd>
</dl>

<dl>
<dd>

**in_reply_to_message_id:** `typing.Optional[str]` — Message-ID of an earlier agent e-mail, to thread the reply
    
</dd>
</dl>

<dl>
<dd>

**as_draft:** `typing.Optional[bool]` — Leave it in the connected Gmail's Drafts instead of sending. Nothing goes out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/alpha/actions/client.py">export_workbook</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Build a styled multi-sheet Excel workbook (.xlsx) from rows you provide, store it in this vault, and return a url plus an artifactId that send_email can attach. Use it when the answer is a table someone will sort, filter or forward. Formatting, freezing and the provenance sheet are automatic. Requires a manager API key, since it stores a file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.actions.export_workbook(
    title="title",
    sheets=[
        {
            "key": "value"
        }
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**title:** `str` — What the workbook is about
    
</dd>
</dl>

<dl>
<dd>

**sheets:** `typing.List[typing.Dict[str, typing.Any]]` — One entry per tab: {name, columns:[{header,key,numFmt?}], rows:[{<key>: value}]}
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[str]` — Where the numbers came from; goes on the provenance sheet
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/alpha/actions/client.py">export_report</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Export a whole dataset from this vault as a file: every finding, or every contradiction, as xlsx, csv or PDF. The only path that produces a PDF. For a table you assembled yourself, use export_workbook. Returns a url and an artifactId that send_email can attach. Requires a manager API key, since it stores a file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.actions.export_report()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**dataset:** `typing.Optional[ExportReportRequestDataset]` — Default findings
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ExportReportRequestFormat]` — Default xlsx
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/alpha/actions/client.py">render_chart</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Render a chart PNG from a Vega-Lite v5 spec with the data inline, and store it as an artifact in this vault. Returns a url to embed and an artifactId that send_email can attach. Do not set colors: the vault's theme is applied automatically. Match the mark to the question. anything over time is a line, a ranking is a sorted horizontal bar, part-of-whole is an arc. Requires a manager API key, since it stores a file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.actions.render_chart(
    title="title",
    vega_lite_spec={
        "key": "value"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**title:** `str` — Chart title, shown on the image
    
</dd>
</dl>

<dl>
<dd>

**vega_lite_spec:** `typing.Dict[str, typing.Any]` — Complete Vega-Lite v5 spec with inline data, e.g. {"data":{"values":[{"month":"2026-05","team":"Logistics","mentions":11}]},"mark":"line","encoding":{...}}. For month buckets set "timeUnit":"yearmonth" or the axis is labelled by day.
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/alpha/actions/client.py">schedule_meeting</a>(...) -> DataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a Google Calendar event with a Meet link via the project's connected calendar. Requires a manager API key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha import Alpha
from alpha.environment import AlphaEnvironment

client = Alpha(
    token="<token>",
    environment=AlphaEnvironment.PRODUCTION,
)

client.actions.schedule_meeting(
    title="title",
    start_iso="startIso",
    attendees=[
        "attendees"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**title:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_iso:** `str` — ISO 8601 with offset, e.g. 2026-07-22T14:00:00-03:00
    
</dd>
</dl>

<dl>
<dd>

**attendees:** `typing.List[str]` — Attendee e-mails
    
</dd>
</dl>

<dl>
<dd>

**vault:** `typing.Optional[str]` — Exact vault id or name from list_vaults. Required whenever the key can reach more than one vault; never guess or use one client's vault for another.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**duration_minutes:** `typing.Optional[float]` — 15 to 120 (default 30)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

