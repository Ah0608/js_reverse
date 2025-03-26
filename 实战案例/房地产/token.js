window = {}

const JSEncrypt = require("jsencrypt");

function get_token() {
    const buildingId = '63097ed0eb04496b8f9306fc408fe554';
    const encrypt = new JSEncrypt();
    encrypt.setPublicKey('MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC1nflpr8o4Jh74z0KPEIBSt+Q4+eCkz6LdyxGZESFgpiQcdIBbWXujhczBCpGO8n1Mo+purvzyxWJIM/I41wjY9JHQSKZF2FL0IfSP8d+V3knz9MA4QHiIzwtrQEpq5U2VmzvSrLsIcPILFPQLZHgaEdQkGVu0NGAzclsMxYmNSQIDAQAB');
    const sProjectId = '930e0442bc60410da837442d9ddb7e02';
    const houseFunctionId = '0';
    const unitType = '';
    const houseStatusId = '0';
    const totalAreaId = '0';
    const inAreaId = '0';

    return  encrypt.encrypt(sProjectId) + "@" + encrypt.encrypt(buildingId) + "@" + encrypt.encrypt(houseFunctionId) + "@" + encrypt.encrypt(unitType) + "@" + encrypt.encrypt(houseStatusId) + "@" + encrypt.encrypt(totalAreaId) + "@" + encrypt.encrypt(inAreaId);
}

console.log(get_token())
