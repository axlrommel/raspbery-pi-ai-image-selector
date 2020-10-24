import express from 'express'
import bodyParser from 'body-parser'
import { analyze } from './analyze'
const jsonParser = bodyParser.json()

const app = express()

app.use('/analyze-image', jsonParser, analyze)

app.listen(3000);
export default app