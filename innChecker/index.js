const express = require('express');
const app = express();
var cors = require('cors')
app.use(cors())
app.set('port', 3041);
app.set('host', '0.0.0.0');
app.listen(app.get('port'), app.get('host'), () => {
    console.log(`[OK] Server is running on ${app.get('host')} :${app.get('port')}`);
});
app.use(express.urlencoded({ extended: true }))
app.use(express.json())

app.use('/api/', require('./routes/index'))