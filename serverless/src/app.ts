import express from 'express'
import cors from 'cors'
import bodyParser from 'body-parser'
import { analyze } from './analyze'
const jsonParser = bodyParser.json()

const app = express()
app.use(cors())

app.use('/analyze-image', jsonParser, analyze)

export default app