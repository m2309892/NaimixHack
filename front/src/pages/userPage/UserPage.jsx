import React from 'react';
import Header from '../../components/Header'
import './userpage.css'
import InnerUser from './Inner';
import Navbar from '../../components/navbar/Navbar';

const UserPage = ({setPage, page, band, setBand}) => {
    


    return(
        <>
        <Navbar setPage={setPage} page={page}/>
        <div className="body">
            <Header/>
            <div className="outline">
                <InnerUser setPage={setPage} page={page} setBand={setBand} band={band}/>
            </div>
        </div>
        </>
    )
}


export default UserPage;
