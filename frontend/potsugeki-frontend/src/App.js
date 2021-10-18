import logo from './logo.svg';
import './App.css';
import Card from './components/Card'
import Form from './containers/Form'
import { useEffect, useState } from 'react';
import axios from 'axios'



function App() {

  const [data,setData] = useState([])
  useEffect(async ()=>{
    const res = await axios(
      "https://potsugeki-z7qgr7dfca-uc.a.run.app/list_clips/kobai"
    )
    console.log(res.data)
    setData(res.data)
  },[])

  return (
    <div className="App">
      <div className='cards_container'>
        {data.map(item => <Card props={item}/>)}
      </div>
      <div className='new_clip'>
        <Form/>
      </div>
    </div>
  );
}

export default App;
