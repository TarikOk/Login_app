import React from 'react';
import {TextField} from '@material-ui/core/';
import {Button} from '@material-ui/core/';
import {withStyles} from "@material-ui/core/styles";


const styles = theme => ({
  root: {
    '& .MuiTextField-root': {
      margin: theme.spacing(1),
      width: '300px',
    },
  },
  border: {
    width: '315px; height: 350px',
    borderRadius: '15px',
    backgroundColor: '#B0E0E6',
    display: 'inline-block',
    marginLeft: "10%",
    marginTop: "200px",
    padding: '30px',
    opacity: '0.7'
  },
  button: {
    '& > *': {
      margin: theme.spacing(1),
      padding: '15px',
      marginTop: '10px',
      width: '300px; height: 55px',
    },
  },
});


class FormRegistr extends React.Component {
  render() {
    const { classes } = this.props;
    return (
      <div className={classes.border}>
      <form className={classes.root} noValidate autoComplete="off" onSubmit={this.props.RegistrData}>
        <div>
          <TextField 
            id="filled-error" 
            label="Login" 
            type="login"
            name="username" 
            variant="filled" />
        </div>
        <div>
          <TextField 
            id="filled-error" 
            label="Email" 
            type="email"
            name="email"
            variant="filled" />
        </div>
        <div>
          <TextField
            id="filled-error"
            label="Password"
            type="password"
            autoComplete="current-password"
            name="password"
            variant="filled"
          />
        </div>
        <div className={classes.button}>
          <Button type="submit" variant="contained" color="primary">Registration</Button>
          <Button onClick={this.props.getFormLogin} variant="outlined" color="primary">I have account</Button>
        </div>
      </form>
      </div>
    );
  };
};

export default withStyles(styles)(FormRegistr);