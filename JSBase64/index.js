import { Base64 } from 'js-base64';
import { Buffer } from 'node:buffer';

const hex = Buffer.from('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d', 'hex')

console.log(Base64.encode(hex));