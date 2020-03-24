import React from 'react';
import './App.css';
import FormLogin from './FormLogin';
import FormRegistr from './FormRegistr';



class App extends React.Component {
  constructor(props) {
    super(props);
    this.onSetLogin = this.onSetLogin.bind(this);
    this.onSetReg = this.onSetReg.bind(this);
    this.state = {isRegistr: false};
  };

  onSetLogin() {
    this.setState({isRegistr: false});
  };

  onSetReg() {
    this.setState({isRegistr: true});
  };

  userReg = async (e) => {
    const request = new FormData(e.target);
    const requestOptions = {
      method: 'POST',
      body: request,
    };
    const response = await fetch(`http://127.0.0.1:8000/auth/users/`, requestOptions);
    const data = await response.json();
    console.log(data);
  };

  userLogin = async (e) => {
    e.preventDefault();
    const request = new FormData(e.target);
    const requestOptions = {
      method: 'POST',
      body: request,
    };
    const response = await fetch(`http://127.0.0.1:8000/auth/token/login/`, requestOptions);
    const data = await response.json();
    console.log(data);
  };

  render() {
    const isRegistr = this.state.isRegistr;
    let check = null;
    if(isRegistr){
      check = <FormRegistr RegistrData={this.userReg} getFormLogin={this.onSetLogin}/>
    } else {
      check = <FormLogin LoginData={this.userLogin} getFormReg={this.onSetReg} />
    }
    return (
      <div>
        {check}
      </div>
    );
  };
};

export default App;


