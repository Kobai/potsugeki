import logo from './logo.svg';
import './App.css';
import { TwitterTweetEmbed} from 'react-twitter-embed'
import Card from './components/Card'
import { useEffect, useState } from 'react';
import axios from 'axios'



function App() {

  const [data,setData] = useState([])
  useEffect(async ()=>{
    const res = await axios(
      "http://192.168.0.14:8080/list_clips/kobai"
    )
    console.log(res.data)
    setData(res.data)
  },[])

  return (
    <div className="App">
      <div className='cards_container'>
        {data.map(item => <Card props={item}/>)}
      </div>
    </div>
  );
}

export default App;
