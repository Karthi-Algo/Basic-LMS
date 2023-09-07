import React, { useEffect, useState } from "react";
import "./MainContainer.css";
import VideoCard from "./VideoCard";

function MainContainer({ videoData, category }) {
  const [categoryList, setCategories] = useState([]);

  function getUniqueListBy(arr, key) {
    return [...new Map(arr.map((item) => [item[key], item])).values()];
  }

  useEffect(() => {
    const arr1 = getUniqueListBy(videoData, "id");
    setCategories(arr1);
  }, [videoData]);

  return (
    <div className="maincontainer">
      <div className="maincontainer__title">
        {categoryList.map((category) => (
          <>
            <div class="chip" id={category.id}>
              {category.topics}
            </div>
            <>
              <div className="maincontainer__videos">
                {videoData.map((v) => {
                  {
                    if (category.topics === v.topics)
                      return (
                        <div>
                          <VideoCard
                            key={v.image_id}
                            ChannelImageUrl={v.channelimage_url}
                            postedDate={v.posted_date}
                            Views={v.views}
                            channelName={v.channel_name}
                            title={v.title}
                            thumbnailUrl={v.thumbnail_url}
                          />
                        </div>
                      );
                  }
                })}
              </div>
            </>
          </>
        ))}
      </div>
    </div>
  );
}

export default MainContainer;
