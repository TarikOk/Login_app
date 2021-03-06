import React from 'react';
import FormLogin from './FormLogin';
import FormRegistr from './FormRegistr';


class Forms extends React.Component {
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
        return( <FormRegistr RegistrData={this.userReg} getFormLogin={this.onSetLogin}/> );
    } else {
        return( <FormLogin LoginData={this.userLogin} getFormReg={this.onSetReg} /> );
    }
  };
};

export default Forms;
