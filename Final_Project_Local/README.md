# Networking and Multimedia Lab - Final Project

This is the final project of Networking and Multimedia Lab. 

Todo: Ensure the docker-compose.yml is suitable.
Todo2: Modify the temporary notebook code.

## Requirement

Same as Pydentity

1. docker
2. docker-compose
3. source-to-image(s2i)

pip package installed in docker container, not need to install in local.

## How to build
```
cd Final_PROJECT_LOCAL
```
run the command at /Networking-and-Multimedia-Lab---Final-Project/FINAL_PROJECT_LOCAL
```
./manage start
```
run the command below at /Networking-and-Multimedia-Lab---Final-Project to get notebook URL
```
./script/get_URLS.sh
```
stop the container, run the command at /Networking-and-Multimedia-Lab---Final-Project/FINAL_PROJECT_LOCAL
```
./manage stop
```

## Task

### 1. Ownership transfer

dir: manufacturer, seller

#### notebook manufacturer/1-Write_DID
When devices producted, the manufacturer creates DID for it and write it to ledger.

#### notebook manufacturer/2-Exchanging_VC, seller/2-Exchanging_VC
After the seller pay money to manufacturer, the manufacturer send a VC to seller.
Run two notebook in the order of MarkDown.

#### notebook manufacturer/3-Verifier, seller/3-Verifier
Someone(customs, hospital) check if the seller own the devices legally.
Run two notebook in the order of MarkDown.

#### notebook manufacturer/4-revocation, seller/3-Verifier, manufacturer/3-Verifier
Sometime manufacturer revoke the credential when discovering devices polluted
Run the revocation notebook and Run the remain two notebook in the order of MarkDown.

### 2. Send Sensitive data (Medical Record) to patients
dir: hospital, the wallet

#### notebook hospital/1-Hospital_Issue_Patient_Data, the_wallet/1-Patient_Accept_Patient_Data
Hospital issue sensitive data to patient wallet.
Run two notebook in th eorder of MarkDown.

### 3. Doctor Send Command to device to do some operations

#### notebook hospital/2-Hospital_Issue_Operation_Command, the_wallet/2-Device_Accept_Operation_Command
Run two notebook in the order of MarkDown.

#### notebook the_wallet/3-Device_wallet medical_device_computer/3-Medical_Device_Computer
Run two notebook in the order of MarkDown