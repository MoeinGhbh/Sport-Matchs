import React, { Component } from 'react';
import './App.css';
// import ViewMatch from './components/ViewMatch';
import axios from 'axios'


class App extends Component{
  constructor(){
    super()
    this.state=[]
  }

//   componentDidMount() {
//     axios.post('http://127.0.0.1:5000/api/v1.0/perRoleHome')
//         .then(res => {
//             if (res.status == 200) {
//                 this.setState({data: res.data.data})
//             }
//         })
//     setInterval(() => axios.post('http://127.0.0.1:5000/api/v1.0/perRoleHome')
//             .then(res => {
//                 if (res.status == 200) {
//                     this.setState({data: res.data.data})
//                 }
//             }).catch(r => {
//                alert('connection is not available')
//             })
//         , 2000)
// }

  render(){
    // const {data} = this.props;

    console.log('asfdasdfas')

    return(
      <div>
      
          {/* <ViewMatch data={this.data} /> */}
      </div>
    );
  }




}

export default App;
