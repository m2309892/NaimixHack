import React from 'react';
import Header from '../../components/Header'
import './comppage.css'
import InnerUser from './Inner';
import Navbar from '../../components/navbar/Navbar';

const СompatibilityPage = ({setPage, page}) => {
    


    return(
        <>
        <Navbar setPage={setPage} page={page}/>
        <div className="body">
            <Header/>
            <div className="outline">
                <InnerUser/>
            </div>
        </div>
        </>
    )
}


export default СompatibilityPage;
