# Engineering Knowledge AI Agent Test

# 1. Describe differences between REST API, MCP in the context of AI.

- Protocol support

MCP supports multiple protocol (HTTP, gRPC, WebSockets, etc. ) in one unified API

REST API limited to one protocol (HTTP)

- Scalability

MCP easier to scale with one unified API across many client types.

REST API scaling means adding more REST endpoints, which adds overhead.

- Flexibility

MCP can adapt to different client needs without separate endpoints.

REST API requires different endpoints or extra APIs to handle varied needs.

- Performance

MCP can choose the most efficient protocol per context (e.g., WebSockets for real-time, GraphQL for complex queries).

REST API performance depends on REST over HTTP; great for standard web services but not always optimal (e.g., chat, streaming)

- Implementation Complexity

Implementing MCP can be more complex initially due to multi-protocol handling.

REST API easier to implement because REST is well known, simple and standardized.

# 2. How REST API, MCP, can improve the AI use case.

REST API makes AI applications more useful by leting the app connect to external systems, such as connecting to external API to search the web, sending/receive data to create transactions, etc.

MCP improves how the AI applications interact with external systems to be more reliable, creating structured access to tools, data, and context in a standardized way.

# 3. How do you ensure that your AI agent answers correctly?

- Describe prompt clearly and use prompting best practices depending on the LLM model (e.g. when using Anthropic Claude 4 model, use this prompting guide from Anthropic: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices) 
- Define and set LLM output schema to make the output more consistent and predictable
- Implement RAG to ground responses with up to date data, and domain specific knowledge
- Enable tool access for the LLM to retrieve information from external system (e.g. a browser tool to retrieve realtime information, database connector for querying structured data, etc.)
- Depending on the use case, LLM may be used only to generate response template (e.g., placeholders or structured outline), and generate full context using downstream processes which are deterministic to prevent hallucinations.

# 4. Describe what can you do with Docker / Containerize environment in the context of AI

***Reproducibility**: Docker ensures that AI models and applications run the same way regardless of where they are deployed.

***Isolation**: Different AI projects can run in separate containers without interfering with each other.

***Scalability**: Easily scale AI applications across containers.

***Resource Efficiency**: Containers use resources more efficiently than VMs, allowing more resources to be dedicated to AI processing.

***Portability**: AI applications in Docker containers can be easily moved between different machines and cloud environments.

***Consistent AI Development Environments**: Ensure that all developers in a team are working in the same environment.

***Experimentation and Testing**: Quickly spin up and tear down different environments for experimentation without affecting the host system.

# 5. How do you finetune the LLM model from raw ?
1. Data Collection
Gather raw text data, clean the data, and tokenize text data using the base model tokenizer

2. Data Formatting
Format text data into specialized format for fine-tuning use case, e.g. formatting data for supervised fine-tuning requires converting raw data into instructions-response pairs.

3. Training Setup
- Choose LLM model to be trained
- Choose fine-tuning strategy whether updating all weights (full fine-tuning) or using Parameter Efficient Fine Tuning (PEFT) which updating only small adapters like LoRA, QLoRA method.
- Estimating the hardware requirements
- Preparing the training hardware like provisioning the VM with certain GPU
- Configuring training hyperparams (learning rate, batch size, max token length)

4. Run Training
Train using formatted dataset, save checkpoints, and monitor training metrics

5. Evaluation & Testing
Evaluate using test cases outside of training data, and monitor metrics

6. Deployment
Serve using nference framework such as vLLM, huggingface inference endpoint, etc..