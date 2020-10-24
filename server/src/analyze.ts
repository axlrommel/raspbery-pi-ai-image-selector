import { propOr } from "ramda";
const tf = require('@tensorflow/tfjs');
// @ts-ignore
global.fetch = require('node-fetch');

const MODEL_URL = 'https://class-website.s3.amazonaws.com/model.json';
const categories = ["cat", "dog"]
const IMAGE_SIZE = 30;

export const analyze = async (req: any, res: any) => {
  try {
    const img: Number[] = propOr([], 'body', req)
    if (img.length) {
      const input = tf.tensor4d(img, [1, IMAGE_SIZE, IMAGE_SIZE, 1]);
      const model = await tf.loadLayersModel(MODEL_URL);
      const prediction = model.predict(input);
      // @ts-ignore
      const result = (await prediction.array())[0];
      console.log(result, categories[result[0] > result[1] ? 0 : 1]);
      res.send(categories[result[0] > result[1] ? 0 : 1]);
    } else {
      console.log('empty body');
      res.send({ status: 'empty body' });
    }
  } catch (error) {
    console.log(error);
    res.send('');
  }
};
