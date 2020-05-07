import React, { Component } from 'react';
import './App.css';
import ViewMatch from './components/ViewMatch';
import axios from 'axios'


class App extends Component{
  constructor(){
    super()
    this.state={
      data:''
    }
  }

  componentDidMount() {
    axios.post('http://127.0.0.1:5000/api/v1.0/getData')
        .then(res => {
            if (res.status == 200) {
                this.setState({data: res.data})
            }
        })
      
    setInterval(() => axios.post('http://127.0.0.1:5000/api/v1.0/getData')
            .then(res => {
                if (res.status == 200) {
                    this.setState({data: res.data})
                }
            }).catch(r => {
               alert('connection is not available')
            })
        , 2000)
}

  render(){
    const {data} = this.state;

    console.log(data)

    return(
      <div>
        <p>this is test of eSport</p>

              {
                    data.map((Zone, index) => {
                        return (
                          <div>
                             <ViewMatch data={this.data} />
                                {/* <ZoneCard
                                    zoneIndex={index}
                                    zoneName={Zone.zoneName}
                                    items={Zone.items}
                                    handler={handler}
                                    zoneId={Zone.zoneId}
                                    className="card"/> */}
                            
                        </div>)
                    })
                }




         
      </div>
    );
  }
}

export default App;
