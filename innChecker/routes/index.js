const express = require('express');
const router = express.Router();
let { parseInnCtrl } = require('../controllers/main')

//get all
router.get('/inn', parseInnCtrl.findOne)

module.exports = router;