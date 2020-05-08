import React, { Component } from 'react';
import './App.css';
import ViewMatch from './components/ViewMatch';
import axios from 'axios'


class App extends Component{
  constructor(){
    super()
    this.state={
      mydata:[]
    }
  }

  componentDidMount() {
    axios.post('http://127.0.0.1:5000/api/v1.0/getData')
  
        .then(res => {
            if (res.status == 200) {
                this.setState({mydata: res.data})
            }
        })
      
    setInterval(() => axios.post('http://127.0.0.1:5000/api/v1.0/getData')
            .then(res => {
                if (res.status == 200) {
                    this.setState({mydata: res.data})
                    console.log(this.state.mydata)
                }
            }).catch(r => {
               alert('connection is not available')
            })
        , 2000)
}

  render(){
    console.log(this.state.mydata,'this.state.mydata')
    // const myObjStr = JSON.stringify(this.state.mydata)
    // console.log(myObjStr,'myobj')

    const arr = []
    Object.keys(this.state.mydata).forEach(key => arr.push({name: key, value: this.state.mydata[key]}))

    return(
      <div>
        <p>this is test of eSport</p>
        
       

         {
        arr.map(item => {
            return (
            <div>
           
              <ViewMatch mydata={item.value} />
            </div>
            )
          })
        }

      </div>
    );
  }
}

export default App;
