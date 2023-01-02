# Networking and Multimedia Lab - Final Project

This is the final project of Networking and Multimedia Lab. 

Todo: Ensure the docker-compose.yml is suitable.
Todo2: Modify the temporary notebook code.

# Define you schema name - must be unique on the ledger
schema_name = "SSI Medical Device"
# Can version the schema if you wish to update it
schema_version = "0.0.1"
# Define any list of attributes you wish to include in your schema
attributes = ["production date","expiration date", "manufacturer", "owner", "type", "status" ]
#production date: datetime object (ref:https://blog.csdn.net/weixin_35834894/article/details/108930202)
#expiration date: datetime object
#manufacturer: string
#owner: string
#type: string (used/unused/defected)
#status: string

response = await agent_controller.schema.write_schema(schema_name, attributes, schema_version)
schema_id = response["schema_id"]
print(schema_id)