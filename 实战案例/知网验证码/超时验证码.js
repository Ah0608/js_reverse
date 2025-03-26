const axios = require('axios');

function redirectNewLink(vValue) {
    const url = `https://kns.cnki.net/kcms2/newLink?v=${vValue}`;
    console.log(url);

    axios.get(url)
        .then(response => {
            const data = response.data;
            if (data) {
                console.log(data);
            }
        })
        .catch(error => {
            return null;
        });
}

const vValue = 'kxaUMs6x7-5BmHdOeA5M_kEjJA_WywJJQacwaUQe8GKhgop5aT5XoJI4dXOOnz7EctXlclWB-AgTVhkXSH2w4sawkkznX_aDSsLZw1eKwj5ARW6SdkALks47_AbzyXSWaE7bxeyol4-28Z00-E9SXCi16Xhweq2EdI0JsdafKyTfamHSp-sSA4WK18OsN_Ce-ErradFN-DZfhA-rEP4LM6YScSKiQyn62L_3WIQwv8AXEW0O95LHr0E2A-4hLoGonv9Xr8rTKEU=';

redirectNewLink(vValue);
