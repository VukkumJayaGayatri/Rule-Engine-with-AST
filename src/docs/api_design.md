# API Design for Rule Engine

## Endpoints

### Create Rule

- **POST** `/create_rule`
- Request Body: 
```json
{
    "rule_string": "<rule>"
}
