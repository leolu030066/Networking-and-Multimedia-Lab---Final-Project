import os
import asyncio
import time

from aries_basic_controller.aries_controller import AriesAgentController

from dotenv import load_dotenv
load_dotenv()

MANUFACTURER_ADMIN_URL = os.getenv('MANUFACTURER_ADMIN_URL')
MANUFACTURER_WEBHOOK_PORT = os.getenv('MANUFACTURER_WEBHOOK_PORT')
MANUFACTURER_WEBHOOK_HOST = os.getenv('MANUFACTURER_WEBHOOK_HOST')
MANUFACTURER_WEBHOOK_BASE = os.getenv('MANUFACTURER_WEBHOOK_BASE')

SELLER_ADMIN_URL = os.getenv('SELLER_ADMIN_URL')
SELLER_WEBHOOK_PORT = os.getenv('SELLER_WEBHOOK_PORT')
SELLER_WEBHOOK_HOST = os.getenv('SELLER_WEBHOOK_HOST')
SELLER_WEBHOOK_BASE = os.getenv('SELLER_WEBHOOK_BASE')

HOSPITAL_ADMIN_URL = os.getenv('HOSPITAL_ADMIN_URL')
HOSPITAL_WEBHOOK_PORT = os.getenv('HOSPITAL_WEBHOOK_PORT')
HOSPITAL_WEBHOOK_HOST = os.getenv('HOSPITAL_WEBHOOK_HOST')
HOSPITAL_WEBHOOK_BASE = os.getenv('HOSPITAL_WEBHOOK_BASE')

MEDICAL_DEVICE_COMPUTER_ADMIN_URL = os.getenv('MEDICAL_DEVICE_COMPUTER_ADMIN_URL')
MEDICAL_DEVICE_COMPUTER_WEBHOOK_PORT = os.getenv('MEDICAL_DEVICE_COMPUTER_WEBHOOK_PORT')
MEDICAL_DEVICE_COMPUTER_WEBHOOK_HOST = os.getenv('MEDICAL_DEVICE_COMPUTER_WEBHOOK_HOST')
MEDICAL_DEVICE_COMPUTER_WEBHOOK_BASE = os.getenv('MEDICAL_DEVICE_COMPUTER_WEBHOOK_BASE')

THE_WALLET_ADMIN_URL = os.getenv('THE_WALLET_ADMIN_URL')
THE_WALLET_WEBHOOK_PORT = os.getenv('THE_WALLET_WEBHOOK_PORT')
THE_WALLET_WEBHOOK_HOST = os.getenv('THE_WALLET_WEBHOOK_HOST')
THE_WALLET_WEBHOOK_BASE = os.getenv('THE_WALLET_WEBHOOK_BASE')


async def start_agent():

    time.sleep(10)

    # Inviter
    seller_agent_controller = AriesAgentController(admin_url=SELLER_ADMIN_URL)

    # Invitee
    manufacturer_agent_controller = AriesAgentController(admin_url=MANUFACTURER_ADMIN_URL)

    # manufacturer_agent_controller.init_webhook_server(
    #                                         webhook_host=MANUFACTURER_WEBHOOK_HOST,
    #                                         webhook_port=MANUFACTURER_WEBHOOK_PORT,
    #                                         webhook_base=MANUFACTURER_WEBHOOK_BASE)

    # await manufacturer_agent_controller.listen_webhooks()
    #
    # await seller_agent_controller.listen_webhooks()
    #
    #
    # seller_agent_controller.register_listeners([], defaults=True)
    # manufacturer_agent_controller.register_listeners([], defaults=True)

    invite = await seller_agent_controller.connections.create_invitation()
    print("Invite from SELLER", invite)

    seller_connection_id = invite["connection_id"]
    print("Bob's connection ID for Alice", seller_connection_id)

    response = await manufacturer_agent_controller.connections.accept_connection(invite["invitation"])


    print("Alice's Connection ID for Bob", response["connection_id"])
    manufacturer_id = response["connection_id"]
    print("Invite Accepted")
    print("Alice's state for Bob's connection :", response["state"])


    time.sleep(10)

    # connection = await seller_agent_controller.connections.get_connection(seller_connection_id)
    # while connection["state"] != "request":
    #     time.sleep(1)
    #     connection = await seller_agent_controller.connections.get_connection(seller_connection_id)

    connection = await seller_agent_controller.connections.get_connection(seller_connection_id)
    print("Bob's Connection State for Alice :", connection["state"])

    all_conns = await seller_agent_controller.connections.get_connections()
    print("All Conns : ", all_conns)


    connection = await seller_agent_controller.connections.accept_request(seller_connection_id)
    print("Request Accepted")
    print(connection)

    print("SELLER AGENT CONNECTION")
    print(connection)

    while connection["state"] != "active":
        trust_ping = await seller_agent_controller.messaging.trust_ping(seller_connection_id, "hello")
        print("TUST PING TO ACTIVATE CONNECTION - SELLER -> RESEARCH")
        print(trust_ping)
        time.sleep(5)
        connection = await seller_agent_controller.connections.get_connection(seller_connection_id)

    trust_ping = await manufacturer_agent_controller.messaging.trust_ping(manufacturer_id,"hello")
    print("TUST PING TO ACTIVATE CONNECTION - RESEARCH -> SELLER")
    print(trust_ping)

    print("MANUFACTURER ID {} SELLER ID {}".format(manufacturer_id, seller_connection_id))

    connection = await seller_agent_controller.connections.get_connection(seller_connection_id)
    print("SELLER AGENT CONNECTION")
    print(connection)

    connection = await manufacturer_agent_controller.connections.get_connection(manufacturer_id)
    print("RESEARCH AGENT CONNECTION")
    print(connection)

    print("SUCCESS")
    time.sleep(2)
    await seller_agent_controller.terminate()
    await manufacturer_agent_controller.terminate()


    time.sleep(10)

    # Inviter
    the_wallet_agent_controller = AriesAgentController(admin_url=THE_WALLET_ADMIN_URL)

    # Invitee
    hospital_agent_controller = AriesAgentController(admin_url=HOSPITAL_ADMIN_URL)

    # manufacturer_agent_controller.init_webhook_server(
    #                                         webhook_host=MANUFACTURER_WEBHOOK_HOST,
    #                                         webhook_port=MANUFACTURER_WEBHOOK_PORT,
    #                                         webhook_base=MANUFACTURER_WEBHOOK_BASE)

    # await manufacturer_agent_controller.listen_webhooks()
    #
    # await seller_agent_controller.listen_webhooks()
    #
    #
    # seller_agent_controller.register_listeners([], defaults=True)
    # manufacturer_agent_controller.register_listeners([], defaults=True)

    invite = await the_wallet_agent_controller.connections.create_invitation()
    print("Invite from SELLER", invite)

    the_wallet_connection_id = invite["connection_id"]
    print("Bob's connection ID for Alice", the_wallet_connection_id)

    response = await hospital_agent_controller.connections.accept_connection(invite["invitation"])


    print("Alice's Connection ID for Bob", response["connection_id"])
    hospital_id = response["connection_id"]
    print("Invite Accepted")
    print("Alice's state for Bob's connection :", response["state"])


    # 
    time.sleep(10)

    # connection = await seller_agent_controller.connections.get_connection(seller_connection_id)
    # while connection["state"] != "request":
    #     time.sleep(1)
    #     connection = await seller_agent_controller.connections.get_connection(seller_connection_id)

    connection = await the_wallet_agent_controller.connections.get_connection(the_wallet_connection_id)
    print("Bob's Connection State for Alice :", connection["state"])

    all_conns = await the_wallet_agent_controller.connections.get_connections()
    print("All Conns : ", all_conns)


    connection = await the_wallet_agent_controller.connections.accept_request(the_wallet_connection_id)
    print("Request Accepted")
    print(connection)

    print("SELLER AGENT CONNECTION")
    print(connection)

    while connection["state"] != "active":
        trust_ping = await the_wallet_agent_controller.messaging.trust_ping(the_wallet_connection_id, "hello")
        print("TUST PING TO ACTIVATE CONNECTION - SELLER -> RESEARCH")
        print(trust_ping)
        time.sleep(5)
        connection = await the_wallet_agent_controller.connections.get_connection(the_wallet_connection_id)

    trust_ping = await hospital_agent_controller.messaging.trust_ping(hospital_id,"hello")
    print("TUST PING TO ACTIVATE CONNECTION - RESEARCH -> SELLER")
    print(trust_ping)

    print("MANUFACTURER ID {} SELLER ID {}".format(hospital_id, the_wallet_connection_id))

    connection = await the_wallet_agent_controller.connections.get_connection(the_wallet_connection_id)
    print("SELLER AGENT CONNECTION")
    print(connection)

    connection = await hospital_agent_controller.connections.get_connection(hospital_id)
    print("RESEARCH AGENT CONNECTION")
    print(connection)

    print("SUCCESS")
    time.sleep(2)
    # await the_wallet_agent_controller.terminate()
    await hospital_agent_controller.terminate()




    time.sleep(10)

    # Inviter
    # the_wallet_agent_controller = AriesAgentController(admin_url=THE_WALLET_ADMIN_URL)

    # Invitee
    medical_device_computer_agent_controller = AriesAgentController(admin_url=MEDICAL_DEVICE_COMPUTER_ADMIN_URL)

    # manufacturer_agent_controller.init_webhook_server(
    #                                         webhook_host=MANUFACTURER_WEBHOOK_HOST,
    #                                         webhook_port=MANUFACTURER_WEBHOOK_PORT,
    #                                         webhook_base=MANUFACTURER_WEBHOOK_BASE)

    # await manufacturer_agent_controller.listen_webhooks()
    #
    # await seller_agent_controller.listen_webhooks()
    #
    #
    # seller_agent_controller.register_listeners([], defaults=True)
    # manufacturer_agent_controller.register_listeners([], defaults=True)

    invite = await the_wallet_agent_controller.connections.create_invitation()
    print("Invite from SELLER", invite)

    the_wallet_connection_id = invite["connection_id"]
    print("Bob's connection ID for Alice", the_wallet_connection_id)

    response = await medical_device_computer_agent_controller.connections.accept_connection(invite["invitation"])


    print("Alice's Connection ID for Bob", response["connection_id"])
    medical_device_computer_id = response["connection_id"]
    print("Invite Accepted")
    print("Alice's state for Bob's connection :", response["state"])


    # 
    time.sleep(10)

    # connection = await seller_agent_controller.connections.get_connection(seller_connection_id)
    # while connection["state"] != "request":
    #     time.sleep(1)
    #     connection = await seller_agent_controller.connections.get_connection(seller_connection_id)

    connection = await the_wallet_agent_controller.connections.get_connection(the_wallet_connection_id)
    print("Bob's Connection State for Alice :", connection["state"])

    all_conns = await the_wallet_agent_controller.connections.get_connections()
    print("All Conns : ", all_conns)


    connection = await the_wallet_agent_controller.connections.accept_request(the_wallet_connection_id)
    print("Request Accepted")
    print(connection)

    print("SELLER AGENT CONNECTION")
    print(connection)

    while connection["state"] != "active":
        trust_ping = await the_wallet_agent_controller.messaging.trust_ping(the_wallet_connection_id, "hello")
        print("TUST PING TO ACTIVATE CONNECTION - SELLER -> RESEARCH")
        print(trust_ping)
        time.sleep(5)
        connection = await the_wallet_agent_controller.connections.get_connection(the_wallet_connection_id)

    trust_ping = await medical_device_computer_agent_controller.messaging.trust_ping(medical_device_computer_id,"hello")
    print("TUST PING TO ACTIVATE CONNECTION - RESEARCH -> SELLER")
    print(trust_ping)

    print("MANUFACTURER ID {} SELLER ID {}".format(medical_device_computer_id, the_wallet_connection_id))

    connection = await the_wallet_agent_controller.connections.get_connection(the_wallet_connection_id)
    print("SELLER AGENT CONNECTION")
    print(connection)

    connection = await medical_device_computer_agent_controller.connections.get_connection(medical_device_computer_id)
    print("RESEARCH AGENT CONNECTION")
    print(connection)

    print("SUCCESS")
    time.sleep(2)
    # await the_wallet_agent_controller.terminate()
    await medical_device_computer_agent_controller.terminate()

if __name__ == "__main__":
    # time.sleep(60)
    try:
        asyncio.get_event_loop().run_until_complete(start_agent())
    except KeyboardInterrupt:
        os._exit(1)
