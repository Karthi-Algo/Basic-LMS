import React from 'react'
import MenuIcon from '@mui/icons-material/Menu';
import TextField from '@mui/material/TextField';
import SearchIcon from '@mui/icons-material/Search';
import NotificationsIcon from '@mui/icons-material/Notifications';
import AppsIcon from '@mui/icons-material/Apps';
import VideoCallIcon from '@mui/icons-material/VideoCall';
import "./Header.css";
import { Button } from '@mui/material';

function Header() {
  return (
    <div className="header">
      {}
      <div className="header__leftSide">
        <MenuIcon/>
        <img className="header__logo"
         src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgrQ__U45rU-mzGoj5pCek8XMcHXZUbTCwwA&usqp=CAU" alt=""/>
      
      </div>
      {}
      <div className="header__search">
        <TextField
        className="header__input" 
        placeholder="Search" variant="outlined"/>
        <Button className="header__searchButton" variant="outlined">
          <SearchIcon/>
        </Button>
       
      </div>
      {}
      <div className="header__rightside">
        <VideoCallIcon/>
        <AppsIcon/>
        <NotificationsIcon/>
       
      </div>
    </div>
  )
}


export default Header
