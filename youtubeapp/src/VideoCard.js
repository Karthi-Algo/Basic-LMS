import React from 'react';
import "./VideoCard.css";

function VideoCard({
    thumbnailUrl,
    ChannelImageUrl,
    title,
    channelName,
    Views,
    postedDate,
    topics
}){
    return(
        <div className="videoCard">
            <img className="videoCard__thumbnail" src={thumbnailUrl} alt=""/>
            <div className="videoCard__info">
              <div className="videoCard__channelImage">
                <img src={ChannelImageUrl} alt=""/>
              </div>
            <div className="videoCard__infoText">
            

                <p className="videoCard__title">{title}</p>
                <p className="videoCard__channelName">{channelName}</p>
                <p className="videoCard__ViewsAndPosteddate">{Views} • {postedDate}</p>

            </div>
            <div className="videoTitle">
                <h1 className="videoTitle__Topics">{topics}</h1>
            </div>

            </div>
        </div>
    )

}
export default VideoCard;